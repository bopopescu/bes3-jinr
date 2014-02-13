#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-wms-job-delete
# Author :  Stuart Paterson
########################################################################
"""
  Reschedule the given DIRAC job
"""
__RCSID__ = "c5c906c (2010-12-17 09:57:46 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
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

  result = dirac.reschedule( job )
  if result['OK']:
    print 'Rescheduled job %s' % ( result['Value'][0] )
  else:
    errorList.append( ( job, result['Message'] ) )
    print result['Message']
    exitCode = 2

for error in errorList:
  print "ERROR %s: %s" % error

DIRAC.exit( exitCode )
