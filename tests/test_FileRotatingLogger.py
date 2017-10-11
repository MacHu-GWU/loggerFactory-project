#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from loggerFactory import FileRotatingLogger


def test():
    path = "log.txt"
    logger = FileRotatingLogger(path=path, max_bytes=1)

    logger.debug("debug")  # nothing
    logger.info("info")  # displayed, but not logged
    logger.warning("warning")  # displayed and logged
    logger.error("error")  # displayed and logged
    logger.critical("critical")  # displayed and logged

    logger.remove_all_handler()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
