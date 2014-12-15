#!/usr/bin/env python

"""Creating lists"""

fruit = [u"Apples",u"Pears",u"Oranges",u"Peaches"]
print(fruit)

#Add a fruit to the list.
more_fruit = raw_input(u"Input another fruit: ")
fruit.append(more_fruit)
print(fruit)
print(len(fruit))

#Number corresponding a fruit in the list.
fruit_number= raw_input(u"Input a number and I'll return the corresponding fruit: ")
try:
    fruit_number=int(fruit_number)
except:
    ValueError or fruit_number<1 or fruit_number>len(fruit)
    while ValueError or fruit_number<1 or fruit_number>len(fruit):
        fruit_number = raw_input(u"Try again. Input a number and I'll return the corresponding fruit: ")
        try:
            fruit_number=int(fruit_number)
            break
        except:
            print("Put in the correct inputs, homie.")
if fruit_number<1 or fruit_number>len(fruit):
    print("You've input a number out of range.") #There has to be a better way to error check for a number between 0-5.

fruit_number = int(fruit_number)
print(fruit[fruit_number-1])

more_fruit = raw_input(u"Input a second fruit: ")
second_fruit = [more_fruit]
fruit=second_fruit+fruit
print(fruit)
more_fruit = raw_input(u"Input a third fruit: ")
fruit.insert(0,more_fruit)
print(fruit)


pfruits=[]
for findp in range(len(fruit)):
    if fruit[findp][0]=="P" or fruit[findp][0]=="p":
        pfruits.append(fruit[findp])

#End of section one for homework.
print(pfruits, "P Fruits list")
pfruits.pop()
print(pfruits, "Removed ending")

pfruits=pfruits*2 #Doubling the list size.

#Identifying which fruit to remove from the list & removing all instances of it.
more_fruit = raw_input(u"Input a fruit to remove: ")
while more_fruit not in pfruits:
    more_fruit = raw_input(u"No instance found. Input a fruit to remove all instances: ")
while more_fruit in pfruits:
    pfruits.remove(more_fruit)

print(pfruits, "After Popcount removal")

userlike = raw_input(u"Do you like %s?" % pfruits[0])
print(userlike)