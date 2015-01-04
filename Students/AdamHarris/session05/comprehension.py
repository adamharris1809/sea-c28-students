#!/usr/bin/env python

"""Return the number of even integers in an inputted array."""

def count_evens(nums):
    return(len([x for x in nums if not x % 2]))