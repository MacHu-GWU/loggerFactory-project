# -*- coding: utf-8 -*-

"""
Implement different type of loggers.
"""

from __future__ import print_function

import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from colorama import Fore, Back, Style

from .rand_str import Charset, rand_str

DEFAULT_LOG_FORMAT = "%(asctime)s; %(levelname)-8s; %(message)s"
DEFAULT_STREAM_FORMAT = "%(message)s"


def get_logger_by_name(
    name=None,
    rand_name=False,
    charset=Charset.HEX,
):
    """
    Get a logger by name.

    :param name: None / str, logger name.
    :param rand_name: if True, ``name`` will be ignored, a random name will be used.
    """
    if rand_name:
        name = rand_str(charset)
    logger = logging.getLogger(name)
    return logger


def set_stream_handler(
    logger,
    stream_level,
    stream_format,
):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_level)
    stream_handler.setFormatter(logging.Formatter(stream_format))
    logger.addHandler(stream_handler)


class BaseLogger(object):
    """
    A base class for logger constructor.
    """
    tab = "    "
    enable_verbose = True
    logger = None

    Fore = Fore
    Back = Back
    Style = Style

    class MessageTemplate(object):
        with_style = "{indent}{style}{msg}" + Style.RESET_ALL

    def __init__(self, name=None, rand_name=False, **kwargs):
        self.logger = get_logger_by_name(name, rand_name)
        self._handler_cache = list()

    def _indent(self, msg, indent):
        return "%s%s" % (self.tab * indent, msg)

    def debug(self, msg, indent=0, **kwargs):
        """invoke ``self.logger.debug``"""
        return self.logger.debug(self._indent(msg, indent), **kwargs)

    def info(self, msg, indent=0, **kwargs):
        """
        invoke ``self.info.debug``
        """
        return self.logger.info(self._indent(msg, indent), **kwargs)

    def warning(self, msg, indent=0, **kwargs):
        """
        invoke ``self.logger.warning``
        """
        return self.logger.warning(self._indent(msg, indent), **kwargs)

    def error(self, msg, indent=0, **kwargs):
        """
        invoke ``self.logger.error``
        """
        return self.logger.error(self._indent(msg, indent), **kwargs)

    def critical(self, msg, indent=0, **kwargs):
        """
        invoke ``self.logger.critical``
        """
        return self.logger.critical(self._indent(msg, indent), **kwargs)

    def show(self, msg, indent=0, style="", **kwargs):
        """
        Print message to console, indent format may apply.
        """
        if self.enable_verbose:
            new_msg = self.MessageTemplate.with_style.format(
                indent=self.tab * indent,
                style=style,
                msg=msg,
            )
            print(new_msg, **kwargs)

    def show_in_red(self, msg, indent=0, **kwargs):
        self.show(msg, indent, Fore.LIGHTRED_EX, **kwargs)

    def show_in_blue(self, msg, indent=0, **kwargs):
        self.show(msg, indent, Fore.LIGHTBLUE_EX, **kwargs)

    def show_in_yellow(self, msg, indent=0, **kwargs):
        self.show(msg, indent, Fore.LIGHTYELLOW_EX, **kwargs)

    def show_in_green(self, msg, indent=0, **kwargs):
        self.show(msg, indent, Fore.GREEN, **kwargs)

    def show_in_cyan(self, msg, indent=0, **kwargs):
        self.show(msg, indent, Fore.CYAN, **kwargs)

    def show_in_meganta(self, msg, indent=0, **kwargs):
        self.show(msg, indent, Fore.MAGENTA, **kwargs)

    __call__ = show

    def remove_all_handler(self):
        """
        Unlink the file handler association.
        """
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
            self._handler_cache.append(handler)

    def recover_all_handler(self):
        """
        Relink the file handler association you just removed.
        """
        for handler in self._handler_cache:
            self.logger.addHandler(handler)
        self._handler_cache = list()


class StreamOnlyLogger(BaseLogger):
    """
    This logger only print message to console, and not write log to files.

    :param stream_level: level above this will be streamed.
    :param stream_format: log information format.

    **中文文档**

    只将日志打印到控制台, 并不将日志信息写入到文件。
    """

    def __init__(
        self,
        name=None,
        rand_name=False,
        stream_level=logging.INFO,
        stream_format=DEFAULT_STREAM_FORMAT,
    ):
        super(StreamOnlyLogger, self).__init__(name, rand_name)

        # Set Logging Level
        self.logger.setLevel(logging.DEBUG)

        # Set Stream Handler
        set_stream_handler(self.logger, stream_level, stream_format)


class SingleFileLogger(BaseLogger):
    """
    This logger print message to console and also write log to files.

    Only one log file will be used.

    :type path: str
    :param path: the absolute path to the log file

    :type reset: bool
    :param reset: if True, the old log content will be removed.

    **中文文档**

    日志被写入到单个文件中。
    """

    def __init__(
        self,
        name=None,
        rand_name=False,
        path=None,
        logging_level=logging.DEBUG,
        stream_level=logging.INFO,
        logging_format=DEFAULT_LOG_FORMAT,
        stream_format=DEFAULT_STREAM_FORMAT,
        reset=False,
    ):
        if path is None:  # pragma: no cover
            raise ValueError("Please specify a log file in ``path``!")

        super(SingleFileLogger, self).__init__(name, rand_name)

        # Set Logging Level
        self.logger.setLevel(logging_level)

        # Set File Handler
        if reset:
            with open(path, "wb") as f:
                pass

        file_handler = logging.FileHandler(
            path, mode="a", encoding="utf-8",
        )
        file_handler.setFormatter(logging.Formatter(logging_format))
        self.logger.addHandler(file_handler)

        # Set Stream Handler
        set_stream_handler(self.logger, stream_level, stream_format)


class FileRotatingLogger(BaseLogger):
    """
    Definition:

    https://docs.python.org/2/library/logging.handlers.html#rotatingfilehandler

    :param path: the absolute path to the log file
    :param max_bytes: max file size.
    :param backup_count: max number of files.

    **中文文档**

    当日志文件的体积大于某个阈值时, 自动重名名, 将日志录入到新的文件中。
    """

    def __init__(
        self,
        name=None,
        rand_name=False,
        path=None,
        logging_level=logging.DEBUG,
        stream_level=logging.INFO,
        logging_format=DEFAULT_LOG_FORMAT,
        stream_format=DEFAULT_STREAM_FORMAT,
        max_bytes=1000000000,  # 1GB
        backup_count=10,
    ):
        if path is None:  # pragma: no cover
            raise ValueError("Please specify a log file in ``path``!")

        super(FileRotatingLogger, self).__init__(name, rand_name)

        # Set Logging Level
        self.logger.setLevel(logging_level)

        # Set File Handler
        file_handler = RotatingFileHandler(
            path, mode="a",
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(logging.Formatter(logging_format))
        self.logger.addHandler(file_handler)

        # Set Stream Handler
        set_stream_handler(self.logger, stream_level, stream_format)


class TimeRotatingLogger(BaseLogger):
    """
    Definition:

    https://docs.python.org/2/library/logging.handlers.html#timedrotatingfilehandler

    :param rotate_on_when: could be "h" (hour), "D" (Day).
    :param interval: rotate on how many hour/day.
    :param backup_count: max number of files.

    **中文文档**

    根据日志发生的时间, 每隔一定时间就更换一个文件名。
    """

    def __init__(
        self,
        name=None,
        rand_name=False,
        path=None,
        logging_level=logging.DEBUG,
        stream_level=logging.INFO,
        logging_format=DEFAULT_LOG_FORMAT,
        stream_format=DEFAULT_STREAM_FORMAT,
        rotate_on_when="D",
        interval=1,
        backup_count=30,
    ):
        if path is None:  # pragma: no cover
            raise ValueError("Please specify a log file in ``path``!")

        super(TimeRotatingLogger, self).__init__(name, rand_name)

        # Set Logging Level
        self.logger.setLevel(logging_level)

        # Set File Handler
        file_handler = TimedRotatingFileHandler(
            path,
            when=rotate_on_when,
            interval=interval,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(logging.Formatter(logging_format))
        self.logger.addHandler(file_handler)

        # Set Stream Handler
        set_stream_handler(self.logger, stream_level, stream_format)
