#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.0.4"
__short_description__ = "Provide several commonly used logger."
__license__ = "MIT"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__maintainer__ = "Sanhe Hu"
__maintainer_email__ = "husanhe@gmail.com"
__github_username__ = "MacHu-GWU"


try:
    from .logger import (
        DebugLevel,
        StreamOnlyLogger,
        SingleFileLogger,
        FileRotatingLogger,
        TimeRotatingLogger,
    )
    from .logfilter import find
except ImportError:  # pragma: no cover
    pass
