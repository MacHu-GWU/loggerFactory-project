# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import pytest
from loggerFactory import SingleFileLogger
from loggerFactory.logfilter import find


def test():
    path = os.path.join(os.path.dirname(__file__), "LogFilter.log")
    logger = SingleFileLogger(path=path, reset=True)
    logger.debug("Debug message")
    logger.info("Info message", 1)
    logger.warning("Warning message", 2)
    logger.error("Error message", 3)
    logger.critical("Critical message", 4)
    logger.remove_all_handler()

    path_result = os.path.join(os.path.dirname(__file__), "result.txt")
    result = find(path, message="info", case_sensitive=False)
    result.dump(path_result)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
