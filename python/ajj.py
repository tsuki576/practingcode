#1 array in python
from array import*

import arrow
vals=array('i',[])
n = int(input("enter the length of the array"))

for i in range(5):
    x=int(input("enter the next value"))
    vals.append(x)

print(vals)
vals=int(input("enter the value for search"))
k=0
for e in vals:
    if e==vals:
        print(e)
        break 
k+=1
print(vals.index[vals])

import numpy
a=numpy.array(["a","b","c","d"])
print(a)