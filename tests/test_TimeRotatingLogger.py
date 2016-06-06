#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loggerFactory import TimeRotatingLogger
import time

def test():
    logger = TimeRotatingLogger("root", "log.txt", rotate_on_when="S")
    
    logger.debug("hello")
    time.sleep(1.0)
    
    logger.info("hello")
    time.sleep(1.0)
    
    logger.warning("hello")
    time.sleep(1.0)
    
    logger.error("hello")
    time.sleep(1.0)
    
    logger.critical("hello")
    time.sleep(1.0)
    
    logger.remove_all_handler()
    
if __name__ == "__main__":
    test()