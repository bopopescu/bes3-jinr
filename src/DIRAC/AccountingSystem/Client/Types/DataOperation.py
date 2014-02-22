# $HeadURL$
__RCSID__ = "bfdd344 (2011-11-02 19:24:01 +0100) Adri Casajs <adria@ecm.ub.es>"

from DIRAC.AccountingSystem.Client.Types.BaseAccountingType import BaseAccountingType
import DIRAC

class DataOperation( BaseAccountingType ):

  def __init__( self ):
    BaseAccountingType.__init__( self )
    self.definitionKeyFields = [ ( 'OperationType' , "VARCHAR(32)" ),
                                 ( 'User', "VARCHAR(32)" ),
                                 ( 'ExecutionSite', 'VARCHAR(32)' ),
                                 ( 'Source', 'VARCHAR(32)' ),
                                 ( 'Destination', 'VARCHAR(32)' ),
                                 ( 'Protocol', 'VARCHAR(32)' ),
                                 ( 'FinalStatus', 'VARCHAR(32)' )
                               ]
    self.definitionAccountingFields = [ ( 'TransferSize', 'BIGINT UNSIGNED' ),
                                        ( 'TransferTime', 'FLOAT' ),
                                        ( 'RegistrationTime', 'FLOAT' ),
                                        ( 'TransferOK', 'INT UNSIGNED' ),
                                        ( 'TransferTotal', 'INT UNSIGNED' ),
                                        ( 'RegistrationOK', 'INT UNSIGNED' ),
                                        ( 'RegistrationTotal', 'INT UNSIGNED' )
                                      ]
    self.bucketsLength = [ ( 86400 * 3, 900 ), #<3d = 15m
                           ( 86400 * 8, 3600 ), #<1w+1d = 1h
                           ( 15552000, 86400 ), #>1w+1d <6m = 1d
                           ( 31104000, 604800 ), #>6m = 1w
                         ]
    self.checkType()
    self.setValueByKey( 'ExecutionSite', DIRAC.siteName() )