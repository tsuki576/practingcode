from random import randrange
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
        print("***error:illegal die number***")