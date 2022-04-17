# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx


def test():
    import loggerFactory

    _ = loggerFactory.StreamOnlyLogger
    _ = loggerFactory.SingleFileLogger
    _ = loggerFactory.FileRotatingLogger
    _ = loggerFactory.TimeRotatingLogger


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
