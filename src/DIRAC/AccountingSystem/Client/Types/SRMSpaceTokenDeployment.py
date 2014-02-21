# $HeadURL$
__RCSID__ = "11175c7 (2011-02-18 15:16:55 +0000) Ricardo Graciani <graciani@ecm.ub.es>"

from DIRAC.AccountingSystem.Client.Types.BaseAccountingType import BaseAccountingType

class SRMSpaceTokenDeployment( BaseAccountingType ):

  def __init__( self ):
    BaseAccountingType.__init__( self )
    self.definitionKeyFields = [ ( 'Site' , "VARCHAR(64)" ),
                                 ( 'Hostname', "VARCHAR(80)" ),
                                 ( 'SpaceTokenDesc', 'VARCHAR(64)' )
                               ]
    self.definitionAccountingFields = [ ( 'AvailableSpace', 'BIGINT UNSIGNED' ),
                                        ( 'UsedSpace', 'BIGINT UNSIGNED' ),
                                        ( 'TotalOnline', 'BIGINT UNSIGNED' ),
                                        ( 'UsedOnline', 'BIGINT UNSIGNED' ),
                                        ( 'FreeOnline', 'BIGINT UNSIGNED' ),
                                        ( 'TotalNearline', 'BIGINT UNSIGNED' ),
                                        ( 'UsedNearline', 'BIGINT UNSIGNED' ),
                                        ( 'FreeNearline', 'BIGINT UNSIGNED' ),
                                        ( 'ReservedNearline', 'BIGINT UNSIGNED' )
                                      ]
    self.bucketsLength = [ ( 15552000, 86400 ), #<6m = 1d
                           ( 31104000, 604800 ), #>6m = 1w
                         ]
    self.checkType()
