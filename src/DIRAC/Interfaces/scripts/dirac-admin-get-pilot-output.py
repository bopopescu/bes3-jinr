#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-admin-get-pilot-output
# Author :  Stuart Paterson
########################################################################
"""
  Retrieve output of a Grid pilot
"""
__RCSID__ = "bbf5710 (2013-07-25 18:13:16 +0200) Stephane Poss <stephposs@gmail.com>"
import DIRAC
from DIRAC.Core.Base import Script


Script.setUsageMessage( '\n'.join( [ __doc__.split( '\n' )[1],
                                     'Usage:',
                                     '  %s [option|cfgfile] ... PilotID ...' % Script.scriptName,
                                     'Arguments:',
                                     '  PilotID:  Grid ID of the pilot' ] ) )
Script.parseCommandLine( ignoreErrors = True )
args = Script.getPositionalArgs()

if len( args ) < 1:
  Script.showHelp()

from DIRAC.Interfaces.API.DiracAdmin                         import DiracAdmin
diracAdmin = DiracAdmin()
exitCode = 0
errorList = []

for gridID in args:

  result = diracAdmin.getPilotOutput( gridID )
  if not result['OK']:
    errorList.append( ( gridID, result['Message'] ) )
    exitCode = 2

for error in errorList:
  print "ERROR %s: %s" % error

DIRAC.exit( exitCode )
