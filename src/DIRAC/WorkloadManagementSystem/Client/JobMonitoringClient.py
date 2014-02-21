""" Class that contains client access to the job monitoring handler. """
########################################################################
# 61d17a7 (2012-12-08 22:27:18 +0100) Andrei Tsaregorodtsev <atsareg@in2p3.fr>
# $HeadURL$
########################################################################
__RCSID__ = "61d17a7 (2012-12-08 22:27:18 +0100) Andrei Tsaregorodtsev <atsareg@in2p3.fr>"

from DIRAC.Core.Base.Client                         import Client
    
class JobMonitoringClient( Client ):
 
  def __init__( self, **kwargs ):
    
    Client.__init__( self, **kwargs )
    self.setServer('WorkloadManagement/JobMonitoring')
