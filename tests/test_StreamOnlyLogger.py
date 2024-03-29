# -*- coding: utf-8 -*-

import pytest
from loggerFactory.logger import StreamOnlyLogger


def test():
    logger = StreamOnlyLogger()
    logger.remove_all_handler()
    logger.recover_all_handler()

    logger.debug("debug", 0)  # not displayed
    logger.info("info", 1)
    logger.warning("warning", 2)
    logger.error("error", 3)
    logger.critical("critical", 4)

    logger("show")  # displayed
    logger.enable_verbose = False  # disable display message
    logger("show")  # not displayed

    logger.remove_all_handler()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
