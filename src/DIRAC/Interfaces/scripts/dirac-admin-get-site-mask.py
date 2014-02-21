#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-admin-get-site-mask
# Author :  Stuart Paterson
########################################################################
__RCSID__ = "7ad103d (2010-12-05 08:04:55 +0000) Andrei Tsaregorodtsev <atsareg@in2p3.fr>"


from DIRAC.Core.Base import Script

Script.setUsageMessage( """
Get the list of sites enabled in the mask for job submission

Usage:
   %s [options]
""" % Script.scriptName )

Script.parseCommandLine( ignoreErrors = True )

import DIRAC
from DIRAC import gLogger
from DIRAC.Interfaces.API.DiracAdmin import DiracAdmin

diracAdmin = DiracAdmin()

gLogger.setLevel('ALWAYS')

result = diracAdmin.getSiteMask(printOutput=True)
if result['OK']:
  DIRAC.exit( 0 )
else:
  print result['Message']
  DIRAC.exit( 2 )

