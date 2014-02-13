#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :   dirac-configuration-cli
# Author : Adria Casajus
########################################################################
"""
  Command line interface to DIRAC Configuration Server
"""
__RCSID__   = "109c68e (2010-11-29 07:11:55 +0000) Ricardo Graciani <graciani@ecm.ub.es>"

import DIRAC
from DIRAC.Core.Base import Script
from DIRAC.ConfigurationSystem.Client.CSCLI import CSCLI

Script.localCfg.addDefaultEntry( "LogLevel", "fatal" )
Script.setUsageMessage('\n'.join( [ __doc__.split( '\n' )[1],
                                    'Usage:',
                                    '  %s [option|cfgfile] ...' % Script.scriptName, ] )   )
Script.parseCommandLine()

CSCLI().start()
