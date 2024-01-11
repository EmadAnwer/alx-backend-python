#!/usr/bin/env python3
""" 5-sum_list.py """

import functools


def sum_list(input_list: list[float]) -> float:
    """sum_list"""

    return functools.reduce(lambda a, b: a + b, input_list)
