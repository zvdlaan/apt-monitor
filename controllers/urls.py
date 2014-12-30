# -*- coding: utf-8 -*-

"""URL definitions of the application. Regex based URLs are mapped to their
class handlers.
"""

from main_handler import IndexHandler
from main_handler import TempsHandler
from main_handler import TempDataHandler
from main_handler import CurrentTempHandler

URLS = (
  '/', IndexHandler,
  '/temps', TempsHandler,
  '/tempData', TempDataHandler,  
  '/tempData/current', CurrentTempHandler
)
