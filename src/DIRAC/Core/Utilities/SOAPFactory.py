# $HeadURL$
__RCSID__ = "5fc7308 (2009-11-26 11:32:29 +0000) Adria Casajus <adria@ecm.ub.es>"

import suds
import urllib2
from DIRAC.Core.DISET.HTTPDISETConnection import HTTPDISETConnection

class DISETHandler( urllib2.HTTPSHandler ):
  
  def https_open(self, req):
    return self.do_open( HTTPDISETConnection, req)
    
class DISETHttpTransport( suds.transport.http.HttpTransport ):
  
  def __init__( self, **kwargs ):
    suds.transport.http.HttpTransport.__init__( self, **kwargs )
    self.handler = DISETHandler()
    self.urlopener = urllib2.build_opener( self.handler )

    
def getSOAPClient( wsdlLocation, **kwargs ):
  kwargs[ 'transport' ] = DISETHttpTransport()
  return suds.client.Client( wsdlLocation, **kwargs )
    
