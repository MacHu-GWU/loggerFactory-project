#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test whether logger can be properly removed.
"""

from loggerFactory import SingleFileLogger

def test():
    logger = SingleFileLogger("root", "log.txt")
    logger.info("Hello") # This display one time
    logger.remove_all_handler()
    
    logger = SingleFileLogger("root", "log.txt")
    logger.info("Good morning") # This displays one time
    logger.remove_all_handler()
    
if __name__ == "__main__":
    test()