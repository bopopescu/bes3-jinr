# $HeadURL$
__RCSID__ = "11175c7 (2011-02-18 15:16:55 +0000) Ricardo Graciani <graciani@ecm.ub.es>"

from DIRAC.AccountingSystem.Client.Types.BaseAccountingType import BaseAccountingType

class Pilot( BaseAccountingType ):

  def __init__( self ):
    BaseAccountingType.__init__( self )
    self.definitionKeyFields = [ ( 'User', 'VARCHAR(32)' ),
                                 ( 'UserGroup', 'VARCHAR(32)' ),
                                 ( 'Site', 'VARCHAR(32)' ),
                                 ( 'GridCE', "VARCHAR(128)" ),
                                 ( 'GridMiddleware', 'VARCHAR(32)' ),
                                 ( 'GridResourceBroker', 'VARCHAR(128)' ),
                                 ( 'GridStatus', 'VARCHAR(32)' ),
                               ]
    self.definitionAccountingFields = [ ( 'Jobs', "INT UNSIGNED" ),
                                      ]
    self.checkType()
