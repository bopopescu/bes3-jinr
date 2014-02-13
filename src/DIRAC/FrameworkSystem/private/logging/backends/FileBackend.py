# $HeadURL$
__RCSID__ = "44175fb (2009-11-06 09:09:35 +0000) Adria Casajus <adria@ecm.ub.es>"
"""  This backend writes the log messages to a file
"""
from DIRAC.FrameworkSystem.private.logging.backends.BaseBackend import BaseBackend

class FileBackend( BaseBackend ):
  def __init__( self, optionsDictionary ):
    self._backendName = "file"
    self._filename = optionsDictionary[ 'FileName' ]

  def doMessage( self, messageObject ):
    try:
      self.file=open( self._filename, 'a' )
    except Exception, v:
      print 'Could not open file %s ' % self._filename
      return 

    self.file.write( "%s\n" % self.composeString( messageObject ) )

    self.file.close()


