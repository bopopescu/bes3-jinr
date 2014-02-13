#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :   dirac-stop-mysql
# Author : Ricardo Graciani
########################################################################
"""
  Stop DIRAC MySQL server
"""
__RCSID__ = "7f45e9c (2010-11-29 14:52:30 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
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
