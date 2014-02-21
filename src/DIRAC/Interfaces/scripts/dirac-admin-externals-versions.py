#!/usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-admin-externals-versions
# Author :  Stuart Paterson
########################################################################
__RCSID__ = "5c9382c (2010-12-14 13:13:33 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
import DIRAC
from DIRAC.Core.Base import Script

Script.parseCommandLine( ignoreErrors = True )

from DIRAC.Interfaces.API.DiracAdmin                         import DiracAdmin
diracAdmin = DiracAdmin()
diracAdmin.getExternalPackageVersions()
DIRAC.exit( 0 )

