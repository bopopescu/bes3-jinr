#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :   dirac-restart-mysql
# Author : Ricardo Graciani
########################################################################
"""
  Restart DIRAC MySQL server
"""
__RCSID__ = "8849fe5 (2010-11-29 13:21:18 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
#
from DIRAC.Core.Base import Script
Script.disableCS()
Script.setUsageMessage( '\n'.join( [ __doc__.split( '\n' )[1],
                                     'Usage:',
                                     '  %s [option|cfgfile] ...' % Script.scriptName,
                                      ] ) )
Script.parseCommandLine()
#
from DIRAC.Core.Utilities import InstallTools
#
InstallTools.exitOnError = True
#
print InstallTools.stopMySQL()['Value'][1]
print InstallTools.startMySQL()['Value'][1]
