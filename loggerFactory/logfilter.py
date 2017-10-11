#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
If your log file is in a standard format, then this module can help you filter
out log information that you care aboue.

**中文文档**

如果你的日志格式是标准的 "%(asctime)s; %(levelname)-8s; %(message)s"。那么本
模块中的函数能够帮助您从日志中轻松的找到你感兴趣的结果。
"""

from __future__ import print_function


class Result(object):
    def __init__(self, path,
                 level, message, time_lower, time_upper, case_sensitive):
        self.path = path
        self.level = level
        self.message = message
        self.time_lower = time_lower
        self.time_upper = time_upper
        self.case_sensitive = case_sensitive

        self.lines = list()

    def __str__(self):
        return self.header + "\n" + "".join(self.lines)

    @property
    def header(self):
        template = ("--- Result of: filepath=%r, level=%r, pattern=%r,"
                    "time_lower=%r, time_upper=%r, case_sensitive=%r ---")
        return template % (self.path,
                           self.level, self.message,
                           self.time_lower, self.time_upper,
                           self.case_sensitive,
                           )

    def dump(self, path):
        with open(path, "wb") as f:
            f.write(str(self).encode("utf-8"))


def find(path,
         level=None,
         message=None,
         time_lower=None, time_upper=None,
         case_sensitive=False):  # pragma: no cover
    """
    Filter log message.

    **中文文档**

    根据level名称, message中的关键字, 和log的时间的区间, 筛选出相关的日志
    """
    if level:
        level = level.upper()  # level name has to be capitalized.

    if not case_sensitive:
        message = message.lower()

    with open(path, "r") as f:
        result = Result(path=path,
                        level=level, message=message,
                        time_lower=time_lower, time_upper=time_upper,
                        case_sensitive=case_sensitive,
                        )

        for line in f:
            try:
                _time, _level, _message = [i.strip() for i in line.split(";")]

                if level:
                    if _level != level:
                        continue

                if time_lower:
                    if _time < time_lower:
                        continue

                if time_upper:
                    if _time > time_upper:
                        continue

                if message:
                    if not case_sensitive:
                        _message = _message.lower()

                    if message not in _message:
                        continue

                result.lines.append(line)
            except Exception as e:
                print(e)

    return result
