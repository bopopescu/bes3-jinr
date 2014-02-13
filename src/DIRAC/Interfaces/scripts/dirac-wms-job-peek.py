#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-wms-job-delete
# Author :  Stuart Paterson
########################################################################
"""
  Peek StdOut of the given DIRAC job
"""
__RCSID__ = "e628c98 (2012-04-27 14:29:57 +0200) Andrei Tsaregorodtsev <atsareg@gmail.com>"
import DIRAC
from DIRAC.Core.Base import Script

Script.setUsageMessage( '\n'.join( [ __doc__.split( '\n' )[1],
                                     'Usage:',
                                     '  %s [option|cfgfile] ... JobID ...' % Script.scriptName,
                                     'Arguments:',
                                     '  JobID:    DIRAC Job ID' ] ) )
Script.parseCommandLine( ignoreErrors = True )
args = Script.getPositionalArgs()

if len( args ) < 1:
  Script.showHelp()

from DIRAC.Interfaces.API.Dirac                              import Dirac
dirac = Dirac()
exitCode = 0
errorList = []

for job in args:

  result = dirac.peek( job, printout=True )
  if not result['OK']:
    errorList.append( ( job, result['Message'] ) )
    exitCode = 2

for error in errorList:
  print "ERROR %s: %s" % error

DIRAC.exit( exitCode )
