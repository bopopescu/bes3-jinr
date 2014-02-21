#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-utils-file-adler
# Author :  
########################################################################
"""
  Calculate alder32 of the supplied file
"""
__RCSID__ = "2b9038b (2010-12-15 07:24:22 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
import DIRAC
from DIRAC.Core.Utilities.Adler     import fileAdler
from DIRAC.Core.Base                import Script

Script.setUsageMessage( '\n'.join( [ __doc__.split( '\n' )[1],
                                     'Usage:',
                                     '  %s [option|cfgfile] ... File ...' % Script.scriptName,
                                     'Arguments:',
                                     '  File:     File Name' ] ) )
Script.parseCommandLine( ignoreErrors = False )
files = Script.getPositionalArgs()
if len( files ) == 0:
  Script.showHelp()

exitCode = 0

for file in files:
  adler = fileAdler( file )
  if adler:
    print file.rjust( 100 ), adler.ljust( 10 )
  else:
    print 'ERROR %s: Failed to get adler' % file
    exitCode = 2

DIRAC.exit( exitCode )
