#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The only file which is directly executed. There's no reason to modify this
file.
"""

import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)

import web
from settings import DEBUG
from controllers.urls import URLS

from tools.app_processor import (header_html, notfound, internalerror)

web.config.debug = DEBUG

app = web.application(URLS, globals(), autoreload=False)
app.notfound = notfound
app.internalerror = internalerror
app.add_processor(web.loadhook(header_html))
application = app.wsgifunc()

if __name__ == '__main__':
  app.run()
