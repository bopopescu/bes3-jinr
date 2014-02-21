########################################################################
# 1e1cd0a (2011-03-18 12:36:58 +0000) Ricardo Graciani <graciani@ecm.ub.es>
########################################################################

""" The LSF TimeLeft utility interrogates the LSF batch system for the
    current CPU and Wallclock consumed, as well as their limits.
"""
__RCSID__ = "1e1cd0a (2011-03-18 12:36:58 +0000) Ricardo Graciani <graciani@ecm.ub.es>"


from DIRAC import gLogger, S_OK, S_ERROR
from DIRAC.Core.Utilities.TimeLeft.TimeLeft import runCommand

from DIRAC.Core.Utilities.Os import sourceEnv

import os, re, time

class LSFTimeLeft:

  #############################################################################
  def __init__( self ):
    """ Standard constructor
    """
    self.log = gLogger.getSubLogger( 'LSFTimeLeft' )
    self.jobID = None
    if os.environ.has_key( 'LSB_JOBID' ):
      self.jobID = os.environ['LSB_JOBID']
    self.queue = None
    if os.environ.has_key( 'LSB_QUEUE' ):
      self.queue = os.environ['LSB_QUEUE']
    self.bin = None
    if os.environ.has_key( 'LSF_BINDIR' ):
      self.bin = os.environ['LSF_BINDIR']
    self.host = None
    if os.environ.has_key( 'LSB_HOSTS' ):
      self.host = os.environ['LSB_HOSTS']
    self.year = time.strftime( '%Y', time.gmtime() )
    self.log.verbose( 'LSB_JOBID=%s, LSB_QUEUE=%s, LSF_BINDIR=%s, LSB_HOSTS=%s' % ( self.jobID,
                                                                                    self.queue,
                                                                                    self.bin,
                                                                                    self.host ) )

    self.cpuLimit = None
    self.cpuRef = None
    self.normRef = None
    self.wallClockLimit = None
    self.hostNorm = None

    cmd = '%s/bqueues -l %s' % ( self.bin, self.queue )
    result = runCommand( cmd )
    if not result['OK']:
      return

    self.log.debug( result['Value'] )
    lines = result['Value'].split( '\n' )
    for i in xrange( len( lines ) ):
      if re.search( '.*CPULIMIT.*', lines[i] ):
        info = lines[i + 1].split()
        if len( info ) >= 4:
          self.cpuLimit = float( info[0] ) * 60
          self.cpuRef = info[3]
        else:
          self.log.warn( 'Problem parsing "%s" for CPU limit' % lines[i + 1] )
          self.cpuLimit = -1
      if re.search( '.*RUNLIMIT.*', lines[i] ):
        info = lines[i + 1].split()
        if len( info ) >= 1:
          self.wallClockLimit = float( info[0] ) * 60
        else:
          self.log.warn( 'Problem parsing "%s" for wall clock limit' % lines[i + 1] )

    modelMaxNorm = 0
    if self.cpuRef:
      # Now try to get the CPU_FACTOR for this reference CPU,
      # it must be either a Model, a Host or the largest Model

      cmd = '%s/lshosts -w %s' % ( self.bin, self.cpuRef )
      result = runCommand( cmd )
      if result['OK']:
        # At CERN this command will return an error since there is no host defined 
        # with the name of the reference Host.
        lines = result['Value'].split( '\n' )
        l1 = lines[0].split()
        l2 = lines[1].split()
        if len( l1 ) > len( l2 ):
          self.log.error( cmd )
          self.log.error( lines[0] )
          self.log.error( lines[1] )
        else:
          for i in range( len( l1 ) ):
            if l1[i] == 'cpuf':
              try:
                self.normRef = float( l2[i] )
                self.log.info( 'Reference Normalization taken from Host', '%s: %s' % ( self.cpuRef, self.normRef ) )
              except Exception:
                pass

      if not self.normRef:
        # Try if there is a model define with the name of cpuRef
        cmd = '%s/lsinfo -m' % ( self.bin )
        result = runCommand( cmd )
        if result['OK']:
          lines = result['Value'].split( '\n' )
          for line in lines[1:]:
            words = line.split()
            if len( words ) > 1:
              try:
                norm = float( words[1] )
                if norm > modelMaxNorm:
                  modelMaxNorm = norm
                if words[0].find( self.cpuRef ) > -1:
                  self.normRef = norm
                  self.log.info( 'Reference Normalization taken from Host Model',
                                 '%s: %s' % ( self.cpuRef, self.normRef ) )
              except:
                pass

      if not self.normRef:
        # Now parse LSF configuration files
        if not os.path.isfile( './lsf.sh' ):
          os.symlink( os.path.join( os.environ['LSF_ENVDIR'], 'lsf.conf' ) , './lsf.sh' )
        ret = sourceEnv( 10, ['./lsf' ] )
        if ret['OK']:
          lsfEnv = ret['outputEnv']
          shared = None
          try:
            egoShared = os.path.join( lsfEnv['LSF_CONFDIR'], 'ego.shared' )
            lsfShared = os.path.join( lsfEnv['LSF_CONFDIR'], 'lsf.shared' )
            if os.path.exists( egoShared ):
              shared = egoShared
            elif os.path.exists( lsfShared ):
              shared = lsfShared
          except Exception:
            pass
          if shared:
            f = open( shared )
            hostModelSection = False
            for line in f.readlines():
              if line.find( 'Begin HostModel' ) == 0:
                hostModelSection = True
                continue
              if not hostModelSection:
                continue
              if line.find( 'End HostModel' ) == 0:
                break
              line = line.strip()
              if line and line.split()[0] == self.cpuRef:
                try:
                  self.normRef = float( line.split()[1] )
                  self.log.info( 'Reference Normalization taken from Configuration File',
                                 '(%s) %s: %s' % ( shared, self.cpuRef, self.normRef ) )
                except Exception:
                  pass
    if not self.normRef:
      # If nothing worked, take the maximum defined for a Model
      if modelMaxNorm:
        self.normRef = modelMaxNorm
        self.log.info( 'Reference Normalization taken from Max Model:', self.normRef )

    # Now get the Normalization for the current Host
    if self.host:
      cmd = '%s/lshosts -w %s' % ( self.bin, self.host )
      result = runCommand( cmd )
      if result['OK']:
        lines = result['Value'].split( '\n' )
        l1 = lines[0].split()
        l2 = lines[1].split()
        if len( l1 ) > len( l2 ):
          self.log.error( cmd )
          self.log.error( lines[0] )
          self.log.error( lines[1] )
        else:
          for i in range( len( l1 ) ):
            if l1[i] == 'cpuf':
              try:
                self.hostNorm = float( l2[i] )
                self.log.info( 'Host Normalization', '%s: %s' % ( self.host, self.hostNorm ) )
              except:
                pass

      if self.hostNorm and self.normRef:
        self.hostNorm = self.hostNorm / self.normRef
        self.log.info( 'CPU Normalization', self.hostNorm )


  #############################################################################
  def getResourceUsage( self ):
    """Returns a dictionary containing CPUConsumed, CPULimit, WallClockConsumed
       and WallClockLimit for current slot.  All values returned in seconds.
    """
    if not self.bin:
      return S_ERROR( 'Could not determine bin directory for LSF' )
    if not self.hostNorm:
      return S_ERROR( 'Could not determine host Norm factor' )


    cpu = None
    wallClock = None

    cmd = '%s/bjobs -W %s' % ( self.bin, self.jobID )
    result = runCommand( cmd )
    if not result['OK']:
      return result
    lines = result['Value'].split( '\n' )
    l1 = lines[0].split()
    l2 = lines[1].split()
    if len( l1 ) > len( l2 ):
      self.log.error( cmd )
      self.log.error( lines[0] )
      self.log.error( lines[1] )
      return S_ERROR( 'Can not parse LSF output' )

    sCPU = None
    sStart = None
    for i in range( len( l1 ) ):
      if l1[i] == 'CPU_USED':
        sCPU = l2[i]
        lCPU = sCPU.split( ':' )
        try:
          cpu = float( lCPU[0] ) * 3600 + float( lCPU[1] ) * 60 + float( lCPU[2] )
        except Exception:
          pass
      elif l1[i] == 'START_TIME':
        sStart = l2[i]
        sStart = '%s %s' % ( sStart, self.year )
        try:
          timeTup = time.strptime( sStart, '%m/%d-%H:%M:%S %Y' )
          wallClock = time.mktime( timeTup )
          wallClock = time.mktime( time.localtime() ) - wallClock
        except Exception:
          pass

    if cpu == None or wallClock == None:
      return S_ERROR( 'Failed to parse LSF output' )

    cpu = cpu * self.hostNorm
    wallClock = wallClock * self.hostNorm

    consumed = {'CPU':cpu, 'CPULimit':self.cpuLimit, 'WallClock':wallClock, 'WallClockLimit':self.wallClockLimit}
    self.log.debug( consumed )
    failed = False
    for key, val in consumed.items():
      if val == None:
        failed = True
        self.log.warn( 'Could not determine %s' % key )

    if not failed:
      return S_OK( consumed )
    else:
      msg = 'Could not determine some parameters,' \
            ' this is the stdout from the batch system call\n%s' % ( result['Value'] )
      self.log.info( msg )
      return S_ERROR( 'Could not determine some parameters' )

#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#
