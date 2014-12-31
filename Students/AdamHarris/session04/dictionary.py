#!/usr/bin/env python

#Part 1

CFdict={'name':'Chris', 'City':'Seattle', 'cake':'chocolate'}
print(CFdict)

CFdict.pop('cake')
print(CFdict)

CFdict['fruit']='Mango'
print(CFdict)

print(CFdict.keys())
print(CFdict.values())

'cake' in CFdict
'Mango' in CFdict


#Part 2

list1=range(14)
list2=[]
for count in list1:
    list2.append(chr(list1[count]))
newdict={} #first 15 hexadecimal strings as keys, 0 to 14 as values.

for x,y in zip(list1,list2):
    newdict[y]=x


#Part 3

ziplist=[]
for count1 in range(len(CFdict.values())):
    a=CFdict.values()[count1].count('a')
    ziplist.append(a)

newdict1={} #values of CFdict as keys; number of a's in each instance as values.
for m,n in zip(ziplist,CFdict.values()):
    newdict1[n]=m

print(newdict1)


#Part 4

s2,s3,s4=set(),set(),set()

for count2 in range(20):
    if count2%2==0:
        s2.update([count2])
    if count2%3==0:
        s3.update([count2])
    if count2%4==0:
        s4.update([count2])
print(s2,s3,s4)

if s3.issubset(s2)==True:
    print("s3 is a subset of s2")
if s4.issubset(s2)==True:
    print("s4 is a subset of s2")

#Part 5

pyset,pyfrozenset=set('Python'),frozenset('marathon')
pyset.update('i')
print("Union: ", pyset.union(pyfrozenset))
print("Intersection: ", pyset.intersection(pyfrozenset))


