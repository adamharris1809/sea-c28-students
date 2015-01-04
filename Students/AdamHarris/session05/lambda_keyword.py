#!/usr/bin/env python

"""Create a function that returns a list of n functions that when called will //
return input value by an increasing number"""

def function_builder(num):
    print([lambda x,y: x+y for y in range(num)])

