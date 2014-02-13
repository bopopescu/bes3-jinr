#! /usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-admin-bdii-cluster
# Author :  Adria Casajus
########################################################################
"""
  Check info on BDII for Cluster
"""
__RCSID__ = "40957c9 (2010-12-10 10:01:23 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
import DIRAC
from DIRAC.Core.Base                                         import Script

Script.registerSwitch( "H:", "host=", "BDII host" )
Script.setUsageMessage( '\n'.join( [ __doc__.split( '\n' )[1],
                                     'Usage:',
                                     '  %s [option|cfgfile] ... CE' % Script.scriptName,
                                     'Arguments:',
                                     '  CE:       Name of the CE(ie: ce111.cern.ch)'] ) )

Script.parseCommandLine( ignoreErrors = True )
args = Script.getPositionalArgs()

from DIRAC.Interfaces.API.DiracAdmin                         import DiracAdmin

if not len( args ) == 1:
  Script.showHelp()

ce = args[0]

host = None

for unprocSw in Script.getUnprocessedSwitches():
  if unprocSw[0] in ( "h", "host" ):
        host = unprocSw[1]

diracAdmin = DiracAdmin()

result = diracAdmin.getBDIICluster( ce, host = host )
if not ['OK']:
  print result['Message']
  DIRAC.exit( 2 )

ces = result['Value']
for ce in ces:
  print "Cluster: %s {" % ce.get( 'GlueClusterName', 'Unknown' )
  for item in ce.iteritems():
    print "%s: %s" % item
  print "}"


