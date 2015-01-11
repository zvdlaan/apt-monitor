# -*- coding: utf-8 -*-

"""URL definitions of the application. Regex based URLs are mapped to their
class handlers.
"""

from main_handler import IndexHandler
from main_handler import TempsHandler
from main_handler import TempDataHandler
from main_handler import CurrentTempHandler
from main_handler import WebcamHandler
from main_handler import BbControlHandler

URLS = (
  '/', IndexHandler,
  '/temps', TempsHandler,
  '/webcam', WebcamHandler,
  '/tempData', TempDataHandler,
  '/tempData/current', CurrentTempHandler,
  '/bbcontrol', BbControlHandler
)
