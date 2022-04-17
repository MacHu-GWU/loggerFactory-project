# -*- coding: utf-8 -*-

from ._version import __version__

__short_description__ = "Provide several commonly used logger."
__license__ = "MIT"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__maintainer__ = "Sanhe Hu"
__maintainer_email__ = "husanhe@gmail.com"
__github_username__ = "MacHu-GWU"

try:
    from .logger import (
        BaseLogger,
        StreamOnlyLogger,
        SingleFileLogger,
        FileRotatingLogger,
        TimeRotatingLogger,
    )
    from .logfilter import find
except ImportError:  # pragma: no cover
    pass
