#!/usr/bin/env python

"""Create a function that returns a list of n functions that when called will //
return input value by an increasing number"""

""" Original attempt added here in comments. The y=y makes sense; didn't recognize the necessity right away.
def function_builder(num):
    return([lambda x,y: x+y for y in range(num)])
"""

def function_builder(num):
    return([lambda x, y=y: x+y for y in range(num)])