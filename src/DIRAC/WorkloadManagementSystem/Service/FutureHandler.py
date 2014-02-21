########################################################################
# $HeadURL$
########################################################################

""" FutureHandler is the implementation of a future
    service in the DISET framework

"""

__RCSID__ = "fef962b (2010-12-13 17:18:13 +0000) Andrei Tsaregorodtsev <atsareg@in2p3.fr>"

from types import *
from DIRAC.Core.DISET.RequestHandler import RequestHandler
from DIRAC import gLogger, S_OK, S_ERROR

def initializeFutureHandler( serviceInfo ):

  return S_OK()

class FutureHandler( RequestHandler ):

  ###########################################################################
  types_echo = [StringType]
  def export_echo(self,input):
    """ Echo input to output
    """

    return S_OK(input) 

