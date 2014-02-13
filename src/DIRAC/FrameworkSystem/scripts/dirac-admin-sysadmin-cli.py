#!/usr/bin/env python
########################################################################
# $HeadURL$
########################################################################
__RCSID__ = "b8c6c57 (2010-07-22 09:45:01 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
from DIRAC.Core.Base import Script

host = None
Script.registerSwitch( "H:", "host=", "   Target host" )
Script.parseCommandLine( ignoreErrors = False )
for switch in Script.getUnprocessedSwitches():
  if switch[0].lower() == "h" or switch[0].lower() == "host":
    host = switch[1]

from DIRAC.FrameworkSystem.Client.SystemAdministratorClientCLI import SystemAdministratorClientCLI

cli = SystemAdministratorClientCLI( host )
cli.cmdloop()
