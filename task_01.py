#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program generates a Fibonacci sequence."""


def xfibo(count):
    """This function generates the Fibonacci sequence.

    Args:
        count(int): Number of integers in the sequence.

    Example:
        >>> for i in xfibo(6):
        print i
        0
        1
        1
        2
        3
        5

    """

    counter = 0
    lastnum, curnum = 0, 1
    while counter < count:
        yield lastnum
        counter += 1
        lastnum, curnum = curnum, lastnum + curnum
