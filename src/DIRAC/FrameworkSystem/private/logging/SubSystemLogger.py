# $HeadURL$
__RCSID__ = "44175fb (2009-11-06 09:09:35 +0000) Adria Casajus <adria@ecm.ub.es>"
import types
from DIRAC.FrameworkSystem.private.logging.LogLevels import LogLevels
from DIRAC.FrameworkSystem.private.logging.Message import Message
from DIRAC.FrameworkSystem.Client.Logger import Logger

class SubSystemLogger( Logger ):

  def __init__( self, subName, mainLogger, child = True ):
    Logger.__init__( self )
    self.__child = child
    for attrName in dir( mainLogger ):
      attrValue = getattr( mainLogger, attrName )
      if type( attrValue ) == types.StringType:
        setattr( self, attrName, attrValue )
    self.__mainLogger = mainLogger
    self._subName = subName

  def processMessage( self, messageObject ):
    if self.__child:
      messageObject.setSubSystemName( self._subName )
    else:
      messageObject.setSystemName( self._subName )
    self.__mainLogger.processMessage( messageObject )
