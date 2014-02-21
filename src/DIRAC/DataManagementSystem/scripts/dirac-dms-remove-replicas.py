#!/usr/bin/env python
########################################################################
# $HeadURL$
########################################################################
__RCSID__ = "3e9dc67 (2013-10-20 08:26:34 +0200) ricardo <Ricardo.Graciani@gmail.com>"
from DIRAC.Core.Base import Script

Script.setUsageMessage( """
Remove the given file replica or a list of file replicas from the File Catalog 
and from the storage.

Usage:
   %s <LFN | fileContainingLFNs> SE [SE]
""" % Script.scriptName )

Script.parseCommandLine()

from DIRAC.Core.Utilities.List                        import sortList, breakListIntoChunks
from DIRAC.DataManagementSystem.Client.ReplicaManager import ReplicaManager
rm = ReplicaManager()
import os, sys

if len( sys.argv ) < 3:
  Script.showHelp()
  DIRAC.exit( -1 )
else:
  inputFileName = sys.argv[1]
  storageElementNames = sys.argv[2:]

if os.path.exists( inputFileName ):
  inputFile = open( inputFileName, 'r' )
  string = inputFile.read()
  lfns = [ lfn.strip() for lfn in string.splitlines() ]
  inputFile.close()
else:
  lfns = [inputFileName]

for lfnList in breakListIntoChunks( sortList( lfns, True ), 500 ):
  for storageElementName in storageElementNames:
    res = rm.removeReplica( storageElementName, lfnList )
    if not res['OK']:
      print 'Error:', res['Message']
    for lfn in sortList( res['Value']['Successful'].keys() ):
      print 'Successfully removed %s replica of %s' % ( storageElementName, lfn )
    for lfn in sortList( res['Value']['Failed'].keys() ):
      message = res['Value']['Failed'][lfn]
      print 'Error: failed to remove %s replica of %s: %s' % ( storageElementName, lfn, message )

