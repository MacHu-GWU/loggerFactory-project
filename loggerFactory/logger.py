#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import string
import random
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

DEFAULT_LOG_FORMAT = "%(asctime)s; %(levelname)-8s; %(message)s"
DEFAULT_STREAM_FORMAT = "%(message)s"


def random_str(charset, length=32):
    """
    Generate random string.
    """
    return "".join([random.choice(charset) for _ in range(length)])


def get_logger_by_name(name=None):
    """
    Get a logger by name. If name is not provided, a random name will be used.
    """
    if name is None:
        name = random_str(string.hexdigits)
    logger = logging.getLogger(name)
    return logger


class DebugLevel(object):
    debug = logging.DEBUG
    info = logging.INFO
    warning = logging.WARNING
    error = logging.ERROR
    critical = logging.CRITICAL


def set_stream_handler(logger, stream_level, stream_format):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_level)
    stream_handler.setFormatter(logging.Formatter(stream_format))
    logger.addHandler(stream_handler)


class BaseLogger(object):
    """A base class for logger constructor.
    """
    tab = "    "
    enable_verbose = True
    _handler_cache = list()
    logger = None

    def debug(self, msg, indent=0):
        """Call logger.debug, indent format may apply.
        """
        self.logger.debug("%s%s" % (self.tab * indent, msg))

    def info(self, msg, indent=0):
        """Call logger.info, indent format may apply.
        """
        self.logger.info("%s%s" % (self.tab * indent, msg))

    def warning(self, msg, indent=0):
        """Call logger.warning, indent format may apply.
        """
        self.logger.warning("%s%s" % (self.tab * indent, msg))

    def error(self, msg, indent=0):
        """Call logger.error, indent format may apply.
        """
        self.logger.error("%s%s" % (self.tab * indent, msg))

    def critical(self, msg, indent=0):
        """Call logger.critical, indent format may apply.
        """
        self.logger.critical("%s%s" % (self.tab * indent, msg))

    def show(self, msg, indent=0):
        """Print message to console, indent format may apply.
        """
        if self.enable_verbose:
            sys.stderr.write("%s%s\n" % (self.tab * indent, msg))

    __call__ = show

    def remove_all_handler(self):
        """Unlink the file handler association.
        """
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
            self._handler_cache.append(handler)

    def recover_all_handler(self):
        """Relink the file handler association you just removed.
        """
        for handler in self._handler_cache:
            self.logger.addHandler(handler)
        self._handler_cache = list()


class StreamOnlyLogger(BaseLogger):
    """This logger only print message to console, and not write log to files.

    :param stream_format： log information format.

    **中文文档**

    只将日志打印到控制台, 并不将日志信息写入到文件。
    """

    def __init__(self, name=None,
                 stream_level=DebugLevel.info,
                 stream_format=DEFAULT_STREAM_FORMAT):
        logger = get_logger_by_name(name)

        # Set Logging Level
        logger.setLevel(logging.DEBUG)

        # Set Stream Handler
        set_stream_handler(logger, stream_level, stream_format)

        self.logger = logger


class SingleFileLogger(BaseLogger):
    """This logger print message to console and also write log to files.

    Only one log file will be used.

    :param reset: boolean, if True, the old log content will be removed.

    **中文文档**

    日志被写入到单个文件中。
    """

    def __init__(self, name=None, path=None,
                 logging_level=DebugLevel.debug,
                 stream_level=DebugLevel.info,
                 logging_format=DEFAULT_LOG_FORMAT,
                 stream_format=DEFAULT_STREAM_FORMAT,
                 reset=False,
                 ):
        logger = get_logger_by_name(name)
        if path is None:  # pragma: no cover
            raise ValueError("Please specify a file as log path!")

        # Set Logging Level
        logger.setLevel(logging_level)

        # Set File Handler
        if reset:
            with open(path, "wb") as f:
                pass

        file_handler = logging.FileHandler(
            path, mode="a", encoding="utf-8",
        )
        file_handler.setFormatter(logging.Formatter(logging_format))
        logger.addHandler(file_handler)

        # Set Stream Handler
        set_stream_handler(logger, stream_level, stream_format)

        self.logger = logger


class FileRotatingLogger(BaseLogger):
    """Definition:

    https://docs.python.org/2/library/logging.handlers.html#rotatingfilehandler

    :param max_bytes: max file size.
    :param backup_count: max number of files.

    **中文文档**

    当日志文件的体积大于某个阈值时, 自动重名名, 将日志录入到新的文件中。
    """

    def __init__(self, name=None, path=None,
                 logging_level=DebugLevel.debug,
                 stream_level=DebugLevel.info,
                 logging_format=DEFAULT_LOG_FORMAT,
                 stream_format=DEFAULT_STREAM_FORMAT,
                 max_bytes=1000000000,  # 1GB
                 backup_count=10,
                 ):
        logger = logging.getLogger(name)
        if path is None:  # pragma: no cover
            raise ValueError("Please specify a file as log path!")

        # Set Logging Level
        logger.setLevel(logging_level)

        # Set File Handler
        file_handler = RotatingFileHandler(
            path, mode="a",
            maxBytes=max_bytes, backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(logging.Formatter(logging_format))
        logger.addHandler(file_handler)

        # Set Stream Handler
        set_stream_handler(logger, stream_level, stream_format)

        self.logger = logger


class TimeRotatingLogger(BaseLogger):
    """Definition:

    https://docs.python.org/2/library/logging.handlers.html#timedrotatingfilehandler

    :param rotate_on_when: could be "h" (hour), "D" (Day).
    :param interval: rotate on how many hour/day.
    :param backup_count: max number of files.

    **中文文档**

    根据日志发生的时间, 每隔一定时间就更换一个文件名。
    """

    def __init__(self, name=None, path=None,
                 logging_level=DebugLevel.debug,
                 stream_level=DebugLevel.info,
                 logging_format=DEFAULT_LOG_FORMAT,
                 stream_format=DEFAULT_STREAM_FORMAT,
                 rotate_on_when="D",
                 interval=1,
                 backup_count=30,
                 ):
        logger = logging.getLogger(name)
        if path is None:  # pragma: no cover
            raise ValueError("Please specify a file as log path!")

        # Set Logging Level
        logger.setLevel(logging_level)

        # Set File Handler
        file_handler = TimedRotatingFileHandler(
            path,
            when=rotate_on_when,
            interval=interval,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(logging.Formatter(logging_format))
        logger.addHandler(file_handler)

        # Set Stream Handler
        set_stream_handler(logger, stream_level, stream_format)

        self.logger = logger
