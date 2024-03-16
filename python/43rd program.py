from random import random,randrange,seed
seed(2)
print("the random number generated is:",random())
for i in range (1,10):
    print(randrange(1,100),end="")