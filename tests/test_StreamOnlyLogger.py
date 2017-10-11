#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from loggerFactory import StreamOnlyLogger


def test():
    logger = StreamOnlyLogger()
    logger.debug("debug", 0)  # not displayed
    logger.info("info", 1)
    logger.warning("warning", 2)
    logger.error("error", 3)
    logger.critical("critical", 4)

    logger("show")
    logger.enable_verbose = False  # disable display message
    logger("show")  # not displayed

    logger.remove_all_handler()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
