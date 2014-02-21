# $HeadURL$
__RCSID__ = "354cb28 (2012-01-11 15:29:00 +0100) Adri Casajs <adria@ecm.ub.es>"

import types
from DIRAC.Core.DISET.private.BaseClient import BaseClient
from DIRAC.Core.Utilities.ReturnValues import S_OK, S_ERROR


class InnerRPCClient( BaseClient ):

  def executeRPC( self, functionName, args ):
    stub = ( self._getBaseStub(), functionName, args )
    retVal = self._connect()
    if not retVal[ 'OK' ]:
      retVal[ 'rpcStub' ] = stub
      return retVal
    trid, transport = retVal[ 'Value' ]
    try:
      retVal = self._proposeAction( transport, ( "RPC", functionName ) )
      if not retVal[ 'OK' ]:
        retVal[ 'rpcStub' ] = stub
        return retVal
      retVal = transport.sendData( S_OK( args ) )
      if not retVal[ 'OK' ]:
        return retVal
      receivedData = transport.receiveData()
      if type( receivedData ) == types.DictType:
        receivedData[ 'rpcStub' ] = stub
      return receivedData
    finally:
      self._disconnect( trid )

