#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-install-mysql
# Author :  Ricardo Graciani
########################################################################
"""
Do the initial installation and configuration of the DIRAC MySQL server
"""
__RCSID__ = "66e9e00 (2010-11-29 12:46:16 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
#
from DIRAC.Core.Utilities import InstallTools
#
InstallTools.exitOnError = True
#
InstallTools.getMySQLPasswords()
#
InstallTools.installMySQL()
#
InstallTools._addMySQLToDiracCfg()