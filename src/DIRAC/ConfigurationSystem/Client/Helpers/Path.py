########################################################################
# $HeadURL$
# File :   Path.py
# Author : Ricardo Graciani
########################################################################
"""
Some Helper class to build CFG paths from tuples
"""
__RCSID__ = "9883c07 (2011-03-06 08:54:02 +0000) Ricardo Graciani <graciani@ecm.ub.es>"

cfgInstallSection = 'LocalInstallation'
cfgResourceSection = 'Resources'

def cfgPath( *args ):
  """
  Basic method to make a path out of a tuple of string, any of them can be already a path
  """
  return '/'.join( [str( k ) for k in args] )

def cfgInstallPath( *args ):
  """
  Path to Installation/Configuration Options
  """
  return cfgPath( cfgInstallSection, *args )

def cfgPathToList( arg ):
  """
  Basic method to split a cfgPath in to a list of strings
  """
  from types import StringTypes
  listPath = []
  if type( arg ) not in StringTypes:
    return listPath
  while arg.find( '/' ) == 0:
    arg = arg[1:]
  return arg.split( '/' )
