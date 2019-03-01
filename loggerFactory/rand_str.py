# -*- coding: utf-8 -*-

import string
import random


class Charset(object):
    ALPHA_LOWER = string.ascii_lowercase
    ALPHA_UPPER = string.ascii_uppercase
    ALPHA = string.ascii_letters
    HEX = "0123456789abcdef"
    ALPHA_DIGITS = string.ascii_letters + string.digits
    PUNCTUATION = string.punctuation


def rand_str(charset, length=32):
    """
    Generate random string.
    """
    return "".join([random.choice(charset) for _ in range(length)])
