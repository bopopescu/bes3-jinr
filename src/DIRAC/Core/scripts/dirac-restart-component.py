#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :   dirac-restart-component
# Author : Ricardo Graciani
########################################################################
"""
  Restart DIRAC component using runsvctrl utility
"""
__RCSID__ = "8849fe5 (2010-11-29 13:21:18 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
#
from DIRAC.Core.Base import Script
Script.disableCS()
Script.setUsageMessage( '\n'.join( [ __doc__.split( '\n' )[1],
                                     'Usage:',
                                     '  %s [option|cfgfile] ... [System [Service|Agent]]' % Script.scriptName,
                                     'Arguments:',
                                     '  System:        Name of the system for the component (default *: all)',
                                     '  Service|Agent: Name of the particular component (default *: all)' ] ) )
Script.parseCommandLine()
args = Script.getPositionalArgs()
if len( args ) > 2:
  Script.showHelp()
  exit( -1 )

system = '*'
component = '*'
if len( args ) > 0:
  system = args[0]
if system != '*':
  if len( args ) > 1:
    component = args[1]
#
from DIRAC.Core.Utilities import InstallTools
#
InstallTools.exitOnError = True
#
result = InstallTools.runsvctrlComponent( system, component, 't' )
if not result['OK']:
  print 'ERROR:', result['Message']
  exit( -1 )

InstallTools.printStartupStatus( result['Value'] )
