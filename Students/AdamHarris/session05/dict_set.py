#!/usr/bin/env python

#Create a dictionary of preferences and pass it to a string format.

food_prefs = {"name": u"Adam",
              u"city": u"Cleveland",
              u"cake": u"chocolate",
              u"fruit": u"apple",
              u"salad": u"caesar",
              u"pasta": u"lasagna"}

print(u"{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta.".format(**food_prefs))


#Create dictionary of zero to fifteen and the hexadecimal equivalent using list comprehension

list1 = range(16)
list2 = [chr(list1[count]) for count in list1]

#This would've been easier had I remembered the dict function exists.
newdict = {list2:list1 for list2,list1 in zip(list2,list1)}

#Create dictionary zero to fifteen and the hexadecimal equivalent using dict comprehension

newdict = {chr(value): value for value in range(16) }

#Create a dictionary that reflects using the same keys as food_prefs but with the number of ‘a’s in each value.
import copy
copy_food_prefs = copy.deepcopy(food_prefs)
copy_food_prefs = {key: value.count('a') for key, value in copy_food_prefs.iteritems()}

#Create sets s2, s3 and s4 that contain the numbers from zero through twenty that are divisible 2, 3 and 4.
s2 = {x for x in range(21) if x%2==0}
s3 = {x for x in range(21) if x%3==0}
s4 = {x for x in range(21) if x%4==0}

#Create a sequence that holds builds all three sets.
"""I spent an eternity trying to add a third iteration to self-generate variables s2,s3,s4.
   I couldn't quite figure it out, but I learned a lot(!)
"""
s2,s3,s4 = [{x for x in range(21) if not x % y} for y in range(2,5)]