#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loggerFactory import SingleFileLogger

logger = SingleFileLogger("root", "log.txt", reset=True)

logger.unlink_logfile() # unlink file association
logger.debug("debug") # nothing
logger.info("info") # displayed, but not logged

logger.relink_logfile() # relink file association 
logger.warning("warning") # displayed and logged
logger.error("error") # displayed and logged
logger.critical("critical") # displayed and logged

logger.unlink_logfile()