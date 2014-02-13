# $HeadURL$
__RCSID__ = "3e8fb84 (2011-02-18 15:45:18 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
import types
from DIRAC import S_OK, S_ERROR, gConfig, gLogger
from DIRAC.FrameworkSystem.DB.SAMDB import SAMDB
from DIRAC.Core.DISET.RequestHandler import RequestHandler

gTestDB = False

def initializeSAMHandler( serviceInfo ):
  global gSAMDB
  gSAMDB = SAMDB()
  return S_OK()

class SAMHandler( RequestHandler ):
  types_doTest = [ types.StringType ]
  def export_doTest( self, typeName ):
    """
      Add a record for a type
    """
    self.log = gLogger.getSubLogger('Test Successfull')
    self.log.info('CALL')
    self.log.info(typeName)
    return S_OK("Return value")
  
  types_setResult = [ types.StringType, types.IntType, types.StringType ]
  def export_setResult(self, result, result_id, description=""):
    """
      Set result for a particular result_id
    """
    self.log = gLogger.getSubLogger('')
    self.log.info('Result ' + result + ' for ' + str(result_id) + ' has been received' )
    result = gSAMDB.setResult(result, result_id, description)
    self.log.info(str(result))
    return S_OK(result)

