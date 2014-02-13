#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-start-mysql
# Author :  Ricardo Graciani
########################################################################
"""
Start DIRAC MySQL server
"""
__RCSID__ = "bb06c87 (2010-11-29 14:56:07 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
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
print InstallTools.startMySQL()['Value'][1]
