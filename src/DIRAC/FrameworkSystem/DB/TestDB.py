########################################################################
# $HeadURL$
########################################################################
""" ProxyRepository class is a front-end to the proxy repository Database
"""

__RCSID__ = "0394cb5 (2012-10-23 15:23:42 +0200) Adri Casajs <adria@ecm.ub.es>"

import time, types
from DIRAC  import gConfig, gLogger, S_OK, S_ERROR
from DIRAC.Core.Utilities import Time
from DIRAC.Core.Base.DB import DB

class TestDB( DB ):

  def __init__( self ):
    DB.__init__( self, 'TestDB', 'Framework/TestDB', 10 )
    retVal = self.__initializeDB()
    if not retVal[ 'OK' ]:
      raise Exception( "Can't create tables: %s" % retVal[ 'Message' ] )

  def __initializeDB( self ):
    """
    Create the tables
    """
    self.__permValues = [ 'USER', 'GROUP', 'VO', 'ALL' ]
    self.__permAttrs = [ 'ReadAccess' ]
    retVal = self._query( "show tables" )
    if not retVal[ 'OK' ]:
      return retVal

    tablesInDB = [ t[0] for t in retVal[ 'Value' ] ]
    tablesD = {}

    if 'up_Users' not in tablesInDB:
      tablesD[ 'up_Users' ] = { 'Fields' : { 'Id' : 'INTEGER AUTO_INCREMENT NOT NULL',
                                             'UserName' : 'VARCHAR(32) NOT NULL',
                                             'LastAccess' : 'DATETIME'
                                            },
                                        'PrimaryKey' : 'Id',
                                      }

    if 'up_Groups' not in tablesInDB:
      tablesD[ 'up_Groups' ] = { 'Fields' : { 'Id' : 'INTEGER AUTO_INCREMENT NOT NULL',
                                              'UserGroup' : 'VARCHAR(32) NOT NULL',
                                              'LastAccess' : 'DATETIME'
                                            },
                                        'PrimaryKey' : 'Id',
                                        'UniqueIndexes' : { 'G' : [ 'UserGroup' ] }
                                      }

    if 'up_VOs' not in tablesInDB:
      tablesD[ 'up_VOs' ] = { 'Fields' : { 'Id' : 'INTEGER AUTO_INCREMENT NOT NULL',
                                           'VO' : 'VARCHAR(32) NOT NULL',
                                           'LastAccess' : 'DATETIME'
                                         },
                                        'PrimaryKey' : 'Id',
                                        'UniqueIndexes' : { 'VO' : [ 'VO' ] }
                                      }

    return self._createTables( tablesD )

  def insert_val( self, val ):
    testKey = str( time.time() )[-31:]
    sqlFieldsName = ['Id', 'UserName', 'LastAccess']
    sqlFieldsValue = [testKey, val, 'UTC_TIMESTAMP()' ]
    
    sqlInsert = "INSERT INTO up_Users (UserName, LastAccess) VALUES ('%s', %s)" % (val, "UTC_TIMESTAMP()")
    print sqlInsert
    gLogger.info(sqlInsert)
    result = self._update( sqlInsert )
    if not result['OK']:
      return result
    return S_OK( result )

  def get_last_val(self):
    selectSQL = "SELECT * FROM up_Users ORDER BY Id  DESC LIMIT 1"
    result = self._query( selectSQL )
    print result
    if not result[ 'OK' ]:
      return result
    return result['Value']

