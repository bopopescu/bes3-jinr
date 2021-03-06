#!/usr/bin/env python
########################################################################
# $Header: $
########################################################################
__RCSID__ = "3e9dc67 (2013-10-20 08:26:34 +0200) ricardo <Ricardo.Graciani@gmail.com>"

from DIRAC.Core.Base import Script

Script.setUsageMessage( """
Remove the given file replica or a list of file replicas from the File Catalog

Usage:
   %s <LFN | fileContainingLFNs>
""" % Script.scriptName )

Script.parseCommandLine()

from DIRAC.Core.Utilities.List import sortList
from DIRAC.DataManagementSystem.Client.ReplicaManager import ReplicaManager
rm = ReplicaManager()
import os, sys

if len( sys.argv ) < 3:
  Script.showHelp()
  DIRAC.exit( -1 )
else:
  inputFileName = sys.argv[1]
  storageElementName = sys.argv[2]

if os.path.exists( inputFileName ):
  inputFile = open( inputFileName, 'r' )
  string = inputFile.read()
  lfns = [ lfn.strip() for lfn in string.splitlines() ]
  inputFile.close()
else:
  lfns = [inputFileName]

res = rm.removeReplicaFromCatalog( storageElementName, lfns )
if not res['OK']:
  print res['Message']
  sys.exit()
for lfn in sortList( res['Value']['Failed'].keys() ):
  message = res['Value']['Failed'][lfn]
  print 'Failed to remove %s replica of %s: %s' % ( storageElementName, lfn, message )
print 'Successfully remove %d catalog replicas at %s' % ( len( res['Value']['Successful'] ), storageElementName )
