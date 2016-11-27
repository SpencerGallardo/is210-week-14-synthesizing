#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 Synthesizing Task 1"""


def xfibo(count):
    """A fibonnaci sequence generator.
    Args:
        count(int): The number of Fibonacci digits to return.
    Returns:
        An iterator.
    Example:
       >>> xfibo(5)
       <generator object xfibo at 0xb60c0914>
       >>> for i in xfibo(5):
       print i
       0
       1
       1
       2
       3
    """
    fiblist = []
    num0, num1 = 0, 1
    while count > len(fiblist):
        fiblist.append(num0)
        yield num0
        num0, num1 = num1, num0 + num1
