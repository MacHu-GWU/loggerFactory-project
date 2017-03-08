#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from loggerFactory import FileRotatingLogger

def test():
    logger = FileRotatingLogger("file_rotating_logger", "log.txt", max_bytes=1)
    
    logger.debug("debug") # nothing
    logger.info("info") # displayed, but not logged
    logger.warning("warning") # displayed and logged
    logger.error("error") # displayed and logged
    logger.critical("critical") # displayed and logged
    
    logger.remove_all_handler()
    
if __name__ == "__main__":
    import os

    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])