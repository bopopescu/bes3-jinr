#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-wms-job-logging-ingo
# Author :  Stuart Paterson
########################################################################
"""
  Retrieve history of transitions for a DIRAC job
"""
__RCSID__ = "d336a21 (2010-12-16 07:25:10 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
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

  result = dirac.loggingInfo( job, printOutput = True )
  if not result['OK']:
    errorList.append( ( job, result['Message'] ) )
    exitCode = 2

for error in errorList:
  print "ERROR %s: %s" % error

DIRAC.exit( exitCode )
