########################################################################
# $HeadURL$
# File :    AgentModule.py
# Author :  Adria Casajus
########################################################################
"""
  Base class for all agent modules
"""
__RCSID__ = "919bc48 (2012-04-19 18:51:40 +0200) Adri Casajs <adria@ecm.ub.es>"

import os
import threading
import types
import time
import DIRAC
from DIRAC import S_OK, S_ERROR, gConfig, gLogger, gMonitor, rootPath
from DIRAC.ConfigurationSystem.Client import PathFinder
from DIRAC.FrameworkSystem.Client.MonitoringClient import MonitoringClient
from DIRAC.Core.Utilities.Shifter import setupShifterProxyInEnv
from DIRAC.Core.Utilities.ReturnValues import isReturnStructure
from DIRAC.Core.Utilities import Time, MemStat

def _checkDir( path ):
  try:
    os.makedirs( path )
  except Exception:
    pass
  if not os.path.isdir( path ):
    raise Exception( 'Can not create %s' % path )

class AgentModule:
  """ Base class for all agent modules

      This class is used by the AgentReactor Class to steer the execution of
      DIRAC Agents.

      For this purpose the following methods are used:
      - am_initialize()      just after instantiated
      - am_getPollingTime()  to set the execution frequency
      - am_getMaxCycles()    to determine the number of cycles
      - am_go()              for the actual execution of one cycle

      Before each iteration, the following methods are used to determine
      if the new cycle is to be started.
      - am_getModuleParam( 'alive' )
      - am_checkStopAgentFile()
      - am_removeStopAgentFile()

      To start new execution cycle the following methods are used
      - am_getCyclesDone()
      - am_setOption( 'MaxCycles', maxCycles )

      At the same time it provides all Agents with common interface.
      All Agent class must inherit from this base class and must implement
      at least the following method:
      - execute()            main method called in the agent cycle

      Additionally they may provide:
      - initialize()         for initial settings
      - finalize()           the graceful exit

      - beginExecution()     before each execution cycle
      - endExecution()       at the end of each execution cycle

      The agent can be stopped either by a signal or by creating a 'stop_agent' file
      in the controlDirectory defined in the agent configuration

  """

  def __init__( self, agentName, loadName, baseAgentName = False, properties = {} ):
    """
      Common __init__ method for all Agents.
      All Agent modules must define:
      __doc__
      __RCSID__
      They are used to populate __codeProperties

      The following Options are used from the Configuration:
      - /LocalSite/InstancePath
      - /DIRAC/Setup
      - Status
      - Enabled
      - PollingTime            default = 120
      - MaxCycles              default = 500
      - ControlDirectory       control/SystemName/AgentName
      - WorkDirectory          work/SystemName/AgentName
      - shifterProxy           ''
      - shifterProxyLocation   WorkDirectory/SystemName/AgentName/.shifterCred

      It defines the following default Options that can be set via Configuration (above):
      - MonitoringEnabled     True
      - Enabled               True if Status == Active
      - PollingTime           120
      - MaxCycles             500
      - ControlDirectory      control/SystemName/AgentName
      - WorkDirectory         work/SystemName/AgentName
      - shifterProxy          False
      - shifterProxyLocation  work/SystemName/AgentName/.shifterCred

      different defaults can be set in the initialize() method of the Agent using am_setOption()

      In order to get a shifter proxy in the environment during the execute()
      the configuration Option 'shifterProxy' must be set, a default may be given
      in the initialize() method.

    """
    if baseAgentName and agentName == baseAgentName:
      self.log = gLogger
      standaloneModule = True
    else:
      self.log = gLogger.getSubLogger( agentName, child = False )
      standaloneModule = False

    self.__basePath = gConfig.getValue( '/LocalSite/InstancePath', rootPath )
    self.__agentModule = None
    self.__codeProperties = {}
    self.__getCodeInfo()

    self.__moduleProperties = { 'fullName' : agentName,
                                'loadName' : loadName,
                                'section' : PathFinder.getAgentSection( agentName ),
                                'loadSection' : PathFinder.getAgentSection( loadName ),
                                'standalone' : standaloneModule,
                                'cyclesDone' : 0,
                                'totalElapsedTime' : 0,
                                'setup' : gConfig.getValue( "/DIRAC/Setup", "Unknown" ),
                                'alive' : True }
    self.__moduleProperties[ 'system' ], self.__moduleProperties[ 'agentName' ] = agentName.split( "/" )
    self.__configDefaults = {}
    self.__configDefaults[ 'MonitoringEnabled'] = True
    self.__configDefaults[ 'Enabled'] = self.am_getOption( "Status", "Active" ).lower() in ( 'active' )
    self.__configDefaults[ 'PollingTime'] = self.am_getOption( "PollingTime", 120 )
    self.__configDefaults[ 'MaxCycles'] = self.am_getOption( "MaxCycles", 500 )
    self.__configDefaults[ 'ControlDirectory' ] = os.path.join( self.__basePath,
                                                                'control',
                                                                *agentName.split( "/" ) )
    self.__configDefaults[ 'WorkDirectory' ] = os.path.join( self.__basePath,
                                                             'work',
                                                             *agentName.split( "/" ) )
    self.__configDefaults[ 'shifterProxy' ] = ''
    self.__configDefaults[ 'shifterProxyLocation' ] = os.path.join( self.__configDefaults[ 'WorkDirectory' ],
                                                                        '.shifterCred' )


    if type( properties ) == types.DictType:
      for key in properties:
        self.__moduleProperties[ key ] = properties[ key ]
      self.__moduleProperties[ 'executors' ] = [ ( self.execute, () ) ]
      self.__moduleProperties[ 'shifterProxy' ] = False

    self.__monitorLastStatsUpdate = -1
    self.monitor = None
    self.__initializeMonitor()
    self.__initialized = False

  def __getCodeInfo( self ):
    versionVar = "__RCSID__"
    docVar = "__doc__"
    try:
      self.__agentModule = __import__( self.__class__.__module__,
                                       globals(),
                                       locals(),
                                       versionVar )
    except Exception:
      self.log.exception( "Cannot load agent module" )
    for prop in ( ( versionVar, "version" ), ( docVar, "description" ) ):
      try:
        self.__codeProperties[ prop[1] ] = getattr( self.__agentModule, prop[0] )
      except Exception:
        self.log.error( "Missing %s" % prop[0] )
        self.__codeProperties[ prop[1] ] = 'unset'
    self.__codeProperties[ 'DIRACVersion' ] = DIRAC.version
    self.__codeProperties[ 'platform' ] = DIRAC.platform

  def am_initialize( self, *initArgs ):
    agentName = self.am_getModuleParam( 'fullName' )
    result = self.initialize( *initArgs )
    if not isReturnStructure( result ):
      return S_ERROR( "initialize must return S_OK/S_ERROR" )
    if not result[ 'OK' ]:
      return S_ERROR( "Error while initializing %s: %s" % ( agentName, result[ 'Message' ] ) )
    _checkDir( self.am_getControlDirectory() )
    _checkDir( self.am_getWorkDirectory() )

    self.__moduleProperties[ 'shifterProxy' ] = self.am_getOption( 'shifterProxy' )
    if self.am_monitoringEnabled():
      self.monitor.enable()
    if len( self.__moduleProperties[ 'executors' ] ) < 1:
      return S_ERROR( "At least one executor method has to be defined" )
    if not self.am_Enabled():
      return S_ERROR( "Agent is disabled via the configuration" )
    self.log.notice( "="*40 )
    self.log.notice( "Loaded agent module %s" % self.__moduleProperties[ 'fullName' ] )
    self.log.notice( " Site: %s" % DIRAC.siteName() )
    self.log.notice( " Setup: %s" % gConfig.getValue( "/DIRAC/Setup" ) )
    self.log.notice( " Base Module version: %s " % __RCSID__ )
    self.log.notice( " Agent version: %s" % self.__codeProperties[ 'version' ] )
    self.log.notice( " DIRAC version: %s" % DIRAC.version )
    self.log.notice( " DIRAC platform: %s" % DIRAC.platform )
    pollingTime = int( self.am_getOption( 'PollingTime' ) )
    if pollingTime > 3600:
      self.log.notice( " Polling time: %s hours" % ( pollingTime / 3600. ) )
    else:
      self.log.notice( " Polling time: %s seconds" % self.am_getOption( 'PollingTime' ) )
    self.log.notice( " Control dir: %s" % self.am_getControlDirectory() )
    self.log.notice( " Work dir: %s" % self.am_getWorkDirectory() )
    if self.am_getOption( 'MaxCycles' ) > 0:
      self.log.notice( " Cycles: %s" % self.am_getMaxCycles() )
    else:
      self.log.notice( " Cycles: unlimited" )
    self.log.notice( "="*40 )
    self.__initialized = True
    return S_OK()

  def am_getControlDirectory( self ):
    return os.path.join( self.__basePath, str( self.am_getOption( 'ControlDirectory' ) ) )

  def am_getStopAgentFile( self ):
    return os.path.join( self.am_getControlDirectory(), 'stop_agent' )

  def am_checkStopAgentFile( self ):
    return os.path.isfile( self.am_getStopAgentFile() )

  def am_createStopAgentFile( self ):
    try:
      fd = open( self.am_getStopAgentFile(), 'w' )
      fd.write( 'Dirac site agent Stopped at %s' % Time.toString() )
      fd.close()
    except Exception:
      pass

  def am_removeStopAgentFile( self ):
    try:
      os.unlink( self.am_getStopAgentFile() )
    except Exception:
      pass

  def am_getBasePath( self ):
    return self.__basePath

  def am_getWorkDirectory( self ):
    return os.path.join( self.__basePath, str( self.am_getOption( 'WorkDirectory' ) ) )

  def am_getShifterProxyLocation( self ):
    return os.path.join( self.__basePath, str( self.am_getOption( 'shifterProxyLocation' ) ) )

  def am_getOption( self, optionName, defaultValue = None ):
    if defaultValue == None:
      if optionName in self.__configDefaults:
        defaultValue = self.__configDefaults[ optionName ]
    if optionName and optionName[0] == "/":
      return gConfig.getValue( optionName, defaultValue )
    for section in ( self.__moduleProperties[ 'section' ], self.__moduleProperties[ 'loadSection' ] ):
      result = gConfig.getOption( "%s/%s" % ( section, optionName ), defaultValue )
      if result[ 'OK' ]:
        return result[ 'Value' ]
    return defaultValue

  def am_setOption( self, optionName, value ):
    self.__configDefaults[ optionName ] = value

  def am_getModuleParam( self, optionName ):
    return self.__moduleProperties[ optionName ]

  def am_setModuleParam( self, optionName, value ):
    self.__moduleProperties[ optionName ] = value

  def am_getPollingTime( self ):
    return self.am_getOption( "PollingTime" )

  def am_getMaxCycles( self ):
    return self.am_getOption( "MaxCycles" )

  def am_getCyclesDone( self ):
    return self.am_getModuleParam( 'cyclesDone' )

  def am_Enabled( self ):
    return self.am_getOption( "Enabled" )

  def am_disableMonitoring( self ):
    self.am_setOption( 'MonitoringEnabled' , False )

  def am_monitoringEnabled( self ):
    return self.am_getOption( "MonitoringEnabled" )

  def am_stopExecution( self ):
    self.am_setModuleParam( 'alive', False )

  def __initializeMonitor( self ):
    """
    Initialize the system monitor client
    """
    if self.__moduleProperties[ 'standalone' ]:
      self.monitor = gMonitor
    else:
      self.monitor = MonitoringClient()
    self.monitor.setComponentType( self.monitor.COMPONENT_AGENT )
    self.monitor.setComponentName( self.__moduleProperties[ 'fullName' ] )
    self.monitor.initialize()
    self.monitor.registerActivity( 'CPU', "CPU Usage", 'Framework', "CPU,%", self.monitor.OP_MEAN, 600 )
    self.monitor.registerActivity( 'MEM', "Memory Usage", 'Framework', 'Memory,MB', self.monitor.OP_MEAN, 600 )
    #Component monitor
    for field in ( 'version', 'DIRACVersion', 'description', 'platform' ):
      self.monitor.setComponentExtraParam( field, self.__codeProperties[ field ] )
    self.monitor.setComponentExtraParam( 'startTime', Time.dateTime() )
    self.monitor.setComponentExtraParam( 'cycles', 0 )
    self.monitor.disable()
    self.__monitorLastStatsUpdate = time.time()

  def am_secureCall( self, functor, args = (), name = False ):
    if not name:
      name = str( functor )
    try:
      result = functor( *args )
      if not isReturnStructure( result ):
        raise Exception( "%s method for %s module has to return S_OK/S_ERROR" % ( name, self.__moduleProperties[ 'fullName' ] ) )
      return result
    except Exception, e:
      self.log.exception( "Exception while calling %s method" % name )
      return S_ERROR( "Exception while calling %s method: %s" % ( name, str( e ) ) )


  def _setShifterProxy( self ):
    if self.__moduleProperties[ "shifterProxy" ]:
      result = setupShifterProxyInEnv( self.__moduleProperties[ "shifterProxy" ],
                                       self.am_getShifterProxyLocation() )
      if not result[ 'OK' ]:
        self.log.error( result['Message'] )
        return result
    return S_OK()

  def am_go( self ):
    #Set the shifter proxy if required
    result = self._setShifterProxy()
    if not result[ 'OK' ]:
      return result
    self.log.notice( "-"*40 )
    self.log.notice( "Starting cycle for module %s" % self.__moduleProperties[ 'fullName' ] )
    mD = self.am_getMaxCycles()
    if mD > 0:
      cD = self.__moduleProperties[ 'cyclesDone' ]
      self.log.notice( "Remaining %s of %s cycles" % ( mD - cD, mD ) )
    self.log.notice( "-"*40 )
    elapsedTime = time.time()
    cpuStats = self._startReportToMonitoring()
    cycleResult = self.__executeModuleCycle()
    if cpuStats:
      self._endReportToMonitoring( *cpuStats )
    #Increment counters
    self.__moduleProperties[ 'cyclesDone' ] += 1
    #Show status
    elapsedTime = time.time() - elapsedTime
    self.__moduleProperties[ 'totalElapsedTime' ] += elapsedTime
    self.log.notice( "-"*40 )
    self.log.notice( "Agent module %s run summary" % self.__moduleProperties[ 'fullName' ] )
    self.log.notice( " Executed %s times previously" % self.__moduleProperties[ 'cyclesDone' ] )
    self.log.notice( " Cycle took %.2f seconds" % elapsedTime )
    averageElapsedTime = self.__moduleProperties[ 'totalElapsedTime' ] / self.__moduleProperties[ 'cyclesDone' ]
    self.log.notice( " Average execution time: %.2f seconds" % ( averageElapsedTime ) )
    elapsedPollingRate = averageElapsedTime * 100 / self.am_getOption( 'PollingTime' )
    self.log.notice( " Polling time: %s seconds" % self.am_getOption( 'PollingTime' ) )
    self.log.notice( " Average execution/polling time: %.2f%%" % elapsedPollingRate )
    if cycleResult[ 'OK' ]:
      self.log.notice( " Cycle was successful" )
    else:
      self.log.error( " Cycle had an error:", cycleResult[ 'Message' ] )
    self.log.notice( "-"*40 )
    #Update number of cycles
    self.monitor.setComponentExtraParam( 'cycles', self.__moduleProperties[ 'cyclesDone' ] )
    return cycleResult

  def _startReportToMonitoring( self ):
    try:
      now = time.time()
      stats = os.times()
      cpuTime = stats[0] + stats[2]
      if now - self.__monitorLastStatsUpdate < 10:
        return ( now, cpuTime )
      # Send CPU consumption mark
      self.__monitorLastStatsUpdate = now
      # Send Memory consumption mark
      membytes = MemStat.VmB( 'VmRSS:' )
      if membytes:
        mem = membytes / ( 1024. * 1024. )
        gMonitor.addMark( 'MEM', mem )
      return( now, cpuTime )
    except Exception:
      return False

  def _endReportToMonitoring( self, initialWallTime, initialCPUTime ):
    wallTime = time.time() - initialWallTime
    stats = os.times()
    cpuTime = stats[0] + stats[2] - initialCPUTime
    percentage = cpuTime / wallTime * 100.
    if percentage > 0:
      gMonitor.addMark( 'CPU', percentage )


  def __executeModuleCycle( self ):
    #Execute the beginExecution function
    result = self.am_secureCall( self.beginExecution, name = "beginExecution" )
    if not result[ 'OK' ]:
      return result
    #Launch executor functions
    executors = self.__moduleProperties[ 'executors' ]
    if len( executors ) == 1:
      result = self.am_secureCall( executors[0][0], executors[0][1] )
      if not result[ 'OK' ]:
        return result
    else:
      exeThreads = [ threading.Thread( target = executor[0], args = executor[1] ) for executor in executors ]
      for thread in exeThreads:
        thread.setDaemon( 1 )
        thread.start()
      for thread in exeThreads:
        thread.join()
    #Execute the endExecution function
    return  self.am_secureCall( self.endExecution, name = "endExecution" )

  def initialize( self, *args, **kwargs ):
    return S_OK()

  def beginExecution( self ):
    return S_OK()

  def endExecution( self ):
    return S_OK()

  def finalize( self ):
    return S_OK()

  def execute( self ):
    return S_ERROR( "Execute method has to be overwritten by agent module" )
