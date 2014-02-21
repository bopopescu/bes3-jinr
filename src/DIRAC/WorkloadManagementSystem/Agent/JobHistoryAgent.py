########################################################################
# $HeadURL$
# File :    JobHistoryAgent.py
# Author :  A.T.
########################################################################
"""
  JobHistoryAgent sends periodically numbers of jobs in various states for various
  sites to the Monitoring system to create historical plots.
"""
__RCSID__ = "74e4f50 (2011-01-18 13:07:33 +0000) Ricardo Graciani <graciani@ecm.ub.es>"

from DIRAC  import gLogger, gMonitor, S_OK, S_ERROR
from DIRAC.Core.Base.AgentModule import AgentModule
from DIRAC.WorkloadManagementSystem.DB.JobDB import JobDB

import time

MONITOR_SITES = ['LCG.CERN.ch', 'LCG.IN2P3.fr', 'LCG.RAL.uk', 'LCG.CNAF.it',
                 'LCG.GRIDKA.de', 'LCG.NIKHEF.nl', 'LCG.PIC.es', 'All sites']
MONITOR_STATUS = ['Running', 'Stalled', 'Done', 'Failed']

class JobHistoryAgent( AgentModule ):
  """
      The specific agents must provide the following methods:
      - initialize() for initial settings
      - beginExecution()
      - execute() - the main method called in the agent cycle
      - endExecution()
      - finalize() - the graceful exit of the method, this one is usually used
                 for the agent restart
  """

  def initialize( self ):

    self.jobDB = JobDB()

    for status in MONITOR_STATUS:
      for site in MONITOR_SITES:
        gLogger.verbose( "Registering activity %s-%s" % ( status, site ) )
        gLogger.verbose( "Jobs in %s state at %s" % ( status, site ) )
        gMonitor.registerActivity( "%s-%s" % ( status, site ), "Jobs in %s state at %s" % ( status, site ),
                                  "JobHistoryAgent", "Jobs/minute", gMonitor.OP_MEAN )

    self.last_update = 0
    self.resultDB = None
    self.reportPeriod = 60
    return S_OK()

  def execute( self ):
    """ Main execution method
    """
    delta = time.time() - self.last_update
    if delta > self.reportPeriod:
      result = self.jobDB.getCounters( 'Jobs', ['Status', 'Site'], {}, '' )
      if not result['OK']:
        return S_ERROR( 'Failed to get data from the Job Database' )
      self.resultDB = result['Value']
      self.last_update = time.time()

    totalDict = {}
    for status in MONITOR_STATUS:
      totalDict[status] = 0

    for row in self.resultDB:
      site = row[0]['Site']
      status = row[0]['Status']
      count = row[1]
      if site in MONITOR_SITES and status in MONITOR_STATUS:
        gLogger.verbose( "Adding mark %s-%s: " % ( status, site ) + str( count ) )
        gMonitor.addMark( "%s-%s" % ( status, site ), count )
      if status in totalDict:
        totalDict[status] += count

    for status in MONITOR_STATUS:
      gLogger.verbose( "Adding mark %s-All sites: " % status + str( totalDict[status] ) )
      gMonitor.addMark( "%s-All sites" % status, totalDict[status] )

    return S_OK()
