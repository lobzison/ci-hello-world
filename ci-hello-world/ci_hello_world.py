"""
Simple module to test CI and test coverage
"""
import math


def my_very_smart_func(num):
    """
    Doing some very complicated logic and algorithms,
    returns sqr of num
    """
    # just testing travis on branch
    # lets break everything with one change
    if num == 0:
        return None
    return math.sqrt(num)
