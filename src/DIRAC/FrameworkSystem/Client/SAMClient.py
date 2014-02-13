from DIRAC import S_OK, S_ERROR, gLogger, gConfig
from DIRAC.Core.DISET.RPCClient                     import RPCClient
from DIRAC.Core.Utilities.ThreadSafe                import Synchronizer

gMonSynchro = Synchronizer()

class SAMClient:
  """
   TestClient
  """

  def __getRPCClient( self ):
    print 'here'
    return RPCClient( "Framework/SAM", timeout = 3600 )

  #@gMonSynchro
  def doTest( self, testType):
    """
    TestFunc
    """
    rpcClient = self.__getRPCClient()
    retVal = rpcClient.doTest( testType )
    return S_OK( retVal )
  #@gMonSynchro
  def setResult(self, result, result_id, description=""):    
    print "Client works"
    rpcClient = self.__getRPCClient()
    result = rpcClient.setResult(result, result_id, description)
    print result
    return S_OK()
 

