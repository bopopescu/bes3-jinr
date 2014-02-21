# $HeadURL$
__RCSID__ = "91f6ef1 (2011-03-18 12:54:31 +0000) Ricardo Graciani <graciani@ecm.ub.es>"

import os
import types

gColors = { 'red':1, 'green':2, 'yellow':3, 'blue':4 }

def colorEnabled():
  if os.environ.has_key( 'TERM' ):
    if os.environ['TERM'] in ( 'xterm', 'xterm-color' ):
      return True
  return False

def colorize( text, color ):
  """Return colorized text"""
  if not colorEnabled():
    return text

  startCode = '\033[;3'
  endCode = '\033[0m'
  if type( color ) == types.IntType:
    return "%s%sm%s%s" % ( startCode, color, text, endCode )
  try:
    return "%s%sm%s%s" % ( startCode, gColors[ color ], text, endCode )
  except:
    return text
