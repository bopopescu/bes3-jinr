########################################################################
# $HeadURL $
# File: DataLoggingClient.py
########################################################################
""" :mod: DataLoggingClient 
    =======================
 
    .. module: DataLoggingClient
    :synopsis: client for DataLoggingDB
"""

## RSCID
__RCSID__ = "61d17a7 (2012-12-08 22:27:18 +0100) Andrei Tsaregorodtsev <atsareg@in2p3.fr>"

## imports
from DIRAC.Core.Base.Client import Client

class DataLoggingClient( Client ):
  """ 
  .. class:: DataLoggingClient

  rpc client for DataLoggingDB 
  """
  def __init__( self, **kwargs  ):
    """ c'tor

    :param self: self reference
    :param str url: service URL
    """
    Client.__init__( self, **kwargs )
    self.setServer( "DataManagement/DataLogging" ) 
    self.setTimeout( 120 )

