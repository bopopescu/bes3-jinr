#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-wms-job-attributes
# Author :  Stuart Paterson
########################################################################
"""
  Retrieve attributes associated with the given DIRAC job
"""
__RCSID__ = "51c752d (2011-02-26 17:53:53 +0000) Stephane Poss <Stephane.Poss@cern.ch>"
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

  result = dirac.attributes( int(job), printOutput = True )
  if not result['OK']:
    errorList.append( ( job, result['Message'] ) )
    exitCode = 2

for error in errorList:
  print "ERROR %s: %s" % error

DIRAC.exit( exitCode )
