#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from loggerFactory import DebugLevel, SingleFileLogger
from util import read_lines


def test():
    path = "SingleFileLogger.log"
    logger = SingleFileLogger(path=path, reset=True)

    logger.remove_all_handler()  # unlink file association
    logger.debug("debug")  # nothing
    logger.info("info")  # displayed, but not logged

    logger.recover_all_handler()  # relink file association
    logger.warning("warning")  # displayed and logged
    logger.error("error")  # displayed and logged
    logger.critical("critical")  # displayed and logged

    logger.remove_all_handler()

    lines = read_lines(path)
    assert len(lines) == 3


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
