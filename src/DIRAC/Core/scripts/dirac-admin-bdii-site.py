#! /usr/bin/env python
########################################################################
# $HeadURL$
# File :    dirac-admin-bdii-site
# Author :  Adria Casajus
########################################################################
"""
  Check info on BDII for Site
"""
__RCSID__ = "3c1211d (2010-12-10 10:02:39 +0000) Ricardo Graciani <graciani@ecm.ub.es>"
import DIRAC
from DIRAC.Core.Base                                         import Script

Script.registerSwitch( "H:", "host=", "BDII host" )
Script.setUsageMessage( '\n'.join( [ __doc__.split( '\n' )[1],
                                     'Usage:',
                                     '  %s [option|cfgfile] ... Site' % Script.scriptName,
                                     'Arguments:',
                                     '  Site:     Name of the Site (ie: CERN-PROD)'] ) )

Script.parseCommandLine( ignoreErrors = True )
args = Script.getPositionalArgs()

from DIRAC.Interfaces.API.DiracAdmin                         import DiracAdmin

if not len( args ) == 1:
  Script.showHelp()

site = args[0]

host = None

for unprocSw in Script.getUnprocessedSwitches():
  if unprocSw[0] in ( "h", "host" ):
        host = unprocSw[1]

diracAdmin = DiracAdmin()

result = diracAdmin.getBDIISite( site, host = host )
if not result['OK']:
  print result['Message']
  DIRAC.exit( 2 )


sites = result['Value']
for site in sites:
  print "Site: %s {" % site.get( 'GlueSiteName', 'Unknown' )
  for item in site.iteritems():
    print "%s: %s" % item
  print "}"


