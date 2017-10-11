#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pytest
from loggerFactory import SingleFileLogger
from loggerFactory.logfilter import find


def test():
    path = "log.txt"
    logger = SingleFileLogger(path=path, reset=True)
    logger.debug("Debug message")
    logger.info("Info message", 1)
    logger.warning("Warning message", 2)
    logger.error("Error message", 3)
    logger.critical("Critical message", 4)
    logger.remove_all_handler()

    result = find("log.txt", message="info", case_sensitive=False)
    result.dump("result.txt")


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
