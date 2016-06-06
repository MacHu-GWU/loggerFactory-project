#!/usr/bin/env python
# -*- coding: utf-8 -*-

from loggerFactory import SingleFileLogger

def test():
    logger = SingleFileLogger("root", "log.txt", reset=True)
    
    logger.remove_all_handler() # unlink file association
    logger.debug("debug") # nothing
    logger.info("info") # displayed, but not logged
    
    logger.recover_all_handler() # relink file association 
    logger.warning("warning") # displayed and logged
    logger.error("error") # displayed and logged
    logger.critical("critical") # displayed and logged
    
    logger.remove_all_handler()
    
#--- Unittest ---
if __name__ == "__main__":
    test()