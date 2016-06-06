#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loggerFactory import StreamOnlyLogger

def test():
    logger = StreamOnlyLogger()
    logger.debug("debug", 0)
    logger.info("info", 1)
    logger.warning("warning", 2)
    logger.error("error", 3)
    logger.critical("critical", 4)
    
    logger.show("show")
    logger.enable_verbose = False # disable display message
    logger.show("show") # nothing
    
    logger.remove_all_handler()
    
if __name__ == "__main__":
    test()