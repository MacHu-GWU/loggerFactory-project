# -*- coding: utf-8 -*-

import os
import pytest
from loggerFactory.logger import SingleFileLogger
from util import read_lines


def test():
    """
    In console, you will see::

        info
        warning
        error
        critical

    In logfile, you will see::

        debug
        info
        warning
        error
        critical
    """
    path = os.path.join(os.path.dirname(__file__), "SingleFile.log")
    logger = SingleFileLogger(rand_name=True, path=path, reset=True)

    logger.debug("debug")  # nothing
    logger.info("info")  # displayed, but not logged
    logger.warning("warning")  # displayed and logged
    logger.error("error")  # displayed and logged
    logger.critical("critical")  # displayed and logged

    logger.remove_all_handler()

    lines = read_lines(path)
    assert len(lines) == 5


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
