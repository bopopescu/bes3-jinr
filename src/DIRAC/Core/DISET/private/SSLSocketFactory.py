# $HeadURL$
__RCSID__ = "518aaa3 (2009-11-23 17:51:57 +0000) Adria Casajus <adria@ecm.ub.es>"

import types
from DIRAC import S_OK, S_ERROR
from DIRAC.Core.DISET.private.Transports.SSL.FakeSocket import FakeSocket
from DIRAC.Core.DISET.private.Transports.SSL.SocketInfoFactory import gSocketInfoFactory
from DIRAC.Core.DISET.private.Transports.SSLTransport import checkSanity

class SSLSocketFactory:

  KW_USE_CERTIFICATES = "useCertificates"
  KW_PROXY_LOCATION = "proxyLocation"
  KW_PROXY_STRING = "proxyString"
  KW_PROXY_CHAIN = "proxyChain"
  KW_SKIP_CA_CHECK = "skipCACheck"
  KW_TIMEOUT = "timeout"
  KW_ENABLE_SESSIONS = 'enableSessions'
  KW_SSL_METHOD = "sslMethod"

  def __checkKWArgs( self, kwargs ):
    for arg, value in ( ( self.KW_TIMEOUT, False ),
                        ( self.KW_ENABLE_SESSIONS, True ),
                        ( self.KW_SSL_METHOD, "SSLv3" ) ):
      if arg not in kwargs:
        kwargs[ arg ] = value

  def createClientSocket( self, addressTuple , **kwargs ):
    if type( addressTuple ) not in ( types.ListType, types.TupleType ):
      return S_ERROR( "hostAdress is not in a tuple form ( 'hostnameorip', port )" )
    self.__checkKWArgs( kwargs )
    result = checkSanity( addressTuple, kwargs )
    if not result[ 'OK' ]:
      return result
    result = gSocketInfoFactory.getSocket( addressTuple, **kwargs )
    if not result[ 'OK' ]:
      return result
    socketInfo = result[ 'Value' ]
    return S_OK( FakeSocket( socketInfo.getSSLSocket(), copies = 1 ) )

gSSLSocketFactory = SSLSocketFactory()