#1

import math

print("Factorial of 7 is:", math.factorial(10))
print("The square root: ",math.sqrt(36))
print("Floor Value:",math.floor(9.6))
print("Ceiling Value:",math.ceil(9.6))
print("Absolote Value:",math.fabs(-536.76))
print("The result of power is:", math.pow(6,3))
print("Log with e:",math.log(100))
print("Log with 100:",math.log10(100))
print()

#2

from random import random,randrange,seed

print("The random number generated is:",random)
print("The random numbers generated using randrange are():")
for i in range(0,24):
    print(randrange(1,100),end=" ")

print()

#3
    
seed(2)
print("The random number generated is:",random)
for i in range(0,24):
    print(randrange(1,100),end=" ")

print()

#4

for i in range(0,4):
    number=randrange(1,6)
    if number==1:
        print("one:*")
    elif number==2:
        print("two:**")
    elif number==3:
        print("three:***")
    elif number==4:
        print("four:****")
    elif number==5:
        print("five:*****")
    elif number==6:
        print("six:******")
    else:
        print("***ERROR: illegal die number***")    