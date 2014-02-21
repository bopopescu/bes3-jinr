#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-install-web-portal
# Author :  Ricardo Graciani
########################################################################
"""
Do the initial installation of a DIRAC Web portal
"""
__RCSID__ = "4fac600 (2010-11-29 12:49:06 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
#
from DIRAC.Core.Utilities import InstallTools
#
InstallTools.exitOnError = True
#
from DIRAC.Core.Base import Script
Script.disableCS()
Script.setUsageMessage('\n'.join( [ __doc__.split( '\n' )[1],
                                    'Usage:',
                                    '  %s [option|cfgfile] ...' % Script.scriptName,
                                    'Arguments:',] ) )

Script.parseCommandLine()

InstallTools.installPortal()
