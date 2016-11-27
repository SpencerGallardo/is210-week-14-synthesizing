#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 Synthesizing Task 2."""

import task_01


def fibo(count):
    """A fibonnaci sequence generator.
    Args:
        count(int): The number of fibonnaci numbers to return.
    Returns:
        A list containing numbers in the fibonnaci sequence up to the count
        number given.
    Examples:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """
    fiblist = []
    for num in task_01.xfibo(count):
        fiblist.append(num)
    return fiblist
