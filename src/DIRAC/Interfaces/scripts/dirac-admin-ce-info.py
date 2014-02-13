#! /usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-admin-ce-info
# Author :  Vladimir Romanovsky
########################################################################
"""
  Retrieve Site Associated to a given CE
"""
__RCSID__ = "dc3cc0a (2010-12-14 13:12:33 +0000) Ricardo Graciani <graciani@ecm.ub.es>"

import DIRAC
from DIRAC.Core.Base import Script
from DIRAC.ConfigurationSystem.Client.Helpers                import cfgPath

grid = 'LCG'

def setGrid( value ):
  global grid
  grid = value
  return DIRAC.S_OK()

Script.registerSwitch( 'G:', 'Grid=', 'Define the Grid where to look (Default: LCG)', setGrid )
Script.setUsageMessage( '\n'.join( [ __doc__.split( '\n' )[1],
                                     'Usage:',
                                     '  %s [option|cfgfile] ... CE ...' % Script.scriptName,
                                     'Arguments:',
                                     '  CE:       Name of the CE' ] ) )

Script.parseCommandLine( ignoreErrors = True )
args = Script.getPositionalArgs()

if len( args ) < 1:
  Script.showHelp()

from DIRAC.Interfaces.API.DiracAdmin                         import DiracAdmin
diracAdmin = DiracAdmin()
exitCode = 0
errorList = []

gridCfgPath = cfgPath( 'Resources', 'Sites', grid )

result = DIRAC.gConfig.getSections( gridCfgPath )
if not result['OK']:
  print 'Could not get DIRAC site list'
  DIRAC.exit( 2 )

sites = result['Value']

for site in sites:
  result = diracAdmin.getCSDict( cfgPath( gridCfgPath, site ) )
  if result['OK']:
    ces = result['Value'].get( 'CE', [] )
    for ce in args:
      if ce in ces:
        print '%s: %s' % ( ce, site )

DIRAC.exit( exitCode )
