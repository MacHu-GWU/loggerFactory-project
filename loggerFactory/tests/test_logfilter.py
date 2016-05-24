#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from loggerFactory import SingleFileLogger
from loggerFactory.logfilter import find


def test():
    logger = SingleFileLogger("root", "log.txt", reset=True)
    logger.debug("Debug message")
    logger.info("Info message", 1)
    logger.warning("Warning message", 2)
    logger.error("Error message", 3)
    logger.critical("Critical message", 4)
    logger.unlink_logfile()

    result = find("log.txt", message="info", case_sensitive=False)
    result.dump("result.txt")
    print(result)


#--- Unittest ---
if __name__ == "__main__":
    test()
