#!/usr/bin/env python

"""Creating lists"""

fruit = [u"Apples",u"Pears",u"Oranges",u"Peaches"]
print(fruit)

#Add a fruit to the list.
more_fruit = raw_input(u"Input another fruit: ")
fruit.append(more_fruit)
print(fruit)
print(len(fruit))
fruitindex = [] #Creating for error checking below

for index in range(len(fruit)):
    fruitindex.append(str(index))
fruitindex.remove("0")

#Number corresponding a fruit in the list.
fruit_number= raw_input(u"Input a number and I'll return the corresponding fruit: ")

while fruit_number not in fruitindex:
    fruit_number = raw_input(u"No such number in list. Input a number and I'll return the corresponding fruit: ")

fruit_number = int(fruit_number)
print(fruit[fruit_number-1])

more_fruit = raw_input(u"Input a second fruit: ")
second_fruit = [more_fruit]
fruit=second_fruit+fruit
print(fruit)
more_fruit = raw_input(u"Input a third fruit: ")
fruit.insert(0,more_fruit)
print(fruit, "Total list of fruit")


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

print(pfruits, "After fruit removal and doubled")

removallist=[] #list of fruits to remove after user completes the questionaire below.
likelist=[] #list of fruits that remains after user identifies their preferences below.
count = 0 #counter
count1 = 0 #second counter
pfruitscopy = pfruits[:] #Creating a copy in order to analyze list results of questionaire

fruitstoquestion = [] #Creating a list of fruits for questionaire below.
for count in range(len(pfruits)):
    while pfruits[count] not in fruitstoquestion:
        fruitstoquestion.append(pfruits[count])

#Questionaire of user preference for fruits.
print(fruitstoquestion, "Fruits to question")

for count1 in range(len(fruitstoquestion)):
    userpref = raw_input(u"Do you like %s? Please respond Yes or No. Trial" % fruitstoquestion[count1])
    while userpref!="Yes" and userpref!="No":
        userpref = raw_input(u"Do you like %s? Please respond Yes or No. No Me Gusta" % fruitstoquestion[count1])
    if userpref == "No":
        while fruitstoquestion[count1] in pfruitscopy:
            pfruitscopy.remove(fruitstoquestion[count1])

"""while userlike not in pfruits:
    while pfruits[count] in removallist:
        count+=1
    while pfruits[count] in likelist:
        count+=1"""

print(pfruits, "Original list")
print(pfruitscopy, "Updated list with user preferences")