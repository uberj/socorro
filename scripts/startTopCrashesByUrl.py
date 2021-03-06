#! /usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import logging
import logging.handlers
import sys
import time

try:
  import config.topCrashesByUrlConfig as configModule
except ImportError:
  import topCrashesByUrlConfig as configModule

import socorro.lib.ConfigurationManager as configurationManager
import socorro.cron.topCrashesByUrl as tcbyurl
import socorro.lib.util as sutil

config = configurationManager.newConfiguration(configurationModule=configModule, applicationName="Top Crash By URL Summary")

logger = logging.getLogger("topCrashesByUrl")
logger.setLevel(logging.DEBUG)

sutil.setupLoggingHandlers(logger, config)
sutil.echoConfig(logger, config)

try:
  before = time.time()
  tu = tcbyurl.TopCrashesByUrl(config)
  tu.processDateInterval()
  logger.info("Successfully ran in %d seconds" % (time.time() - before))
finally:
  logger.info("done.")
