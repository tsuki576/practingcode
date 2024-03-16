x=int(input("enter your choice : 1 for odd, 2 for even:"))
if x==1:
    print("first five odd numbers are:")
    for a in range(1,11,2):
        print(a)
elif x==2:
    print("first five even numbers are:")
    for a in range(2,11,2):
        print(a)
else:
    print("input is wrong")