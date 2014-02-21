# $HeadURL$
__RCSID__ = "ccd22d9 (2012-01-25 17:02:47 +0100) ricardo <Ricardo.Graciani@gmail.com>"

from DIRAC                                              import S_OK, S_ERROR, gConfig
from DIRAC.ConfigurationSystem.Client.Helpers.Path      import cfgPath

gBaseLocalSiteSection = "/LocalSite"

def gridEnv():
  """
    Return location of gridenv file to get a UI environment
  """
  return gConfig.getValue( cfgPath( gBaseLocalSiteSection, 'GridEnv' ), '' )
