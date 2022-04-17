# -*- coding: utf-8 -*-


def read_lines(path):
    with open(path, "r") as f:
        return [line.strip() for line in f]
