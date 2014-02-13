#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-proxy-init.py
# Author :  Adrian Casajus
###########################################################from DIRAC.Core.Base import Script#############
__RCSID__ = "ffeb152 (2011-11-29 10:13:45 +0100) Adria Casajus <adria@ecm.ub.es>"

import sys
import DIRAC
from DIRAC.Core.Base import Script
from DIRAC.FrameworkSystem.Client.ProxyUpload import CLIParams, uploadProxy

if __name__ == "__main__":
  cliParams = CLIParams()
  cliParams.registerCLISwitches()

  Script.parseCommandLine()

  retVal = uploadProxy( cliParams )
  if not retVal[ 'OK' ]:
    print retVal[ 'Message' ]
    sys.exit( 1 )
  sys.exit( 0 )
