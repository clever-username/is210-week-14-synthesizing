#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program uses comprehension and returns list (Fibonacci seq)."""

import task_01


def fibo(count):
    """This function returns a (list) Fibonacci sequence.
    Args:
        None
    Example:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """
    return [item for item in task_01.xfibo(count)]
