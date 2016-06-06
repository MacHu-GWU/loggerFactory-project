#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loggerFactory import FileRotatingLogger

def test():
    logger = FileRotatingLogger("root", "log.txt", max_bytes=1)
    
    logger.debug("debug") # nothing
    logger.info("info") # displayed, but not logged
    logger.warning("warning") # displayed and logged
    logger.error("error") # displayed and logged
    logger.critical("critical") # displayed and logged
    
    logger.remove_all_handler()
    
if __name__ == "__main__":
    test()