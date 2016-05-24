#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loggerFactory import FileRotatingLogger

logger = FileRotatingLogger("root", "log.txt", max_bytes=1000000)

logger.debug("debug") # nothing
logger.info("info") # displayed, but not logged
logger.warning("warning") # displayed and logged
logger.error("error") # displayed and logged
logger.critical("critical") # displayed and logged

logger.unlink_logfile()