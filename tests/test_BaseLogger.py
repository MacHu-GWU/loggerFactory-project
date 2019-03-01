# -*- coding: utf-8 -*-

import pytest
from loggerFactory.logger import BaseLogger


def test():
    logger = BaseLogger()
    logger.show_in_red("Hello", indent=0)
    logger.show_in_blue("Hello", indent=1)
    logger.show_in_yellow("Hello", indent=2)
    logger.show_in_green("Hello", indent=3)
    logger.show_in_cyan("Hello", indent=4)
    logger.show_in_meganta("Hello", indent=5)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
