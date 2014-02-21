#! /usr/bin/env python
########################################################################
# $HeadURL: $
########################################################################
__RCSID__   = "$Id:  $"

from DIRAC.Core.Base import Script 

Script.setUsageMessage("""
Clean the given directory or a list of directories by removing it and all the
contained files and subdirectories from the physical storage and from the
file catalogs.

Usage:
   %s <lfn | fileContainingLfns> <SE> <status>
""" % Script.scriptName)

Script.parseCommandLine()
import sys,os

from DIRAC.Core.Utilities.List import sortList,randomize

if len(sys.argv) < 2:
  Script.showHelp()
  DIRAC.exit( -1 )
else:
  inputFileName = sys.argv[1]

if os.path.exists(inputFileName):
  inputFile = open(inputFileName,'r')
  string = inputFile.read()
  lfns = sortList(string.splitlines(),True)
  inputFile.close()
else:
  lfns = [inputFileName]

from DIRAC.DataManagementSystem.Client.ReplicaManager import ReplicaManager
rm = ReplicaManager()
for lfn in sortList(lfns):
  lfn = lfn.strip()
  if not lfn: continue
  print "Cleaning directory %s ... " % lfn,
  sys.stdout.flush()
  result = rm.cleanLogicalDirectory(lfn)
  if result['OK']:
    print 'OK'
  else:
    print "ERROR: %s" % result['Message']  
