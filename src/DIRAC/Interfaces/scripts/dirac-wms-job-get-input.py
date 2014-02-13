#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-production-job-get-input
# Author :  Stuart Paterson
########################################################################
"""
  Retrieve input sandbox for DIRAC Job
"""
__RCSID__ = "d336a21 (2010-12-16 07:25:10 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
import DIRAC
from DIRAC.Core.Base import Script
import os

Script.setUsageMessage( '\n'.join( [ __doc__.split( '\n' )[1],
                                     'Usage:',
                                     '  %s [option|cfgfile] ... JobID ...' % Script.scriptName,
                                     'Arguments:',
                                     '  JobID:    DIRAC Job ID' ] ) )
Script.registerSwitch( "D:", "Dir=", "Store the output in this directory" )
Script.parseCommandLine( ignoreErrors = True )
args = Script.getPositionalArgs()

if len( args ) < 1:
  Script.showHelp()

from DIRAC.Interfaces.API.Dirac                              import Dirac
dirac = Dirac()
exitCode = 0
errorList = []

outputDir = None
for sw, v in Script.getUnprocessedSwitches():
  if sw in ( 'D', 'Dir' ):
    outputDir = v

for job in args:

  result = dirac.getInputSandbox( job, outputDir = outputDir )
  if result['OK']:
    if os.path.exists( 'InputSandbox%s' % job ):
      print 'Job input sandbox retrieved in InputSandbox%s/' % ( job )
  else:
    errorList.append( ( job, result['Message'] ) )
    exitCode = 2

for error in errorList:
  print "ERROR %s: %s" % error

DIRAC.exit( exitCode )
