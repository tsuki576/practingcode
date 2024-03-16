a= eval(input("enter your choice 1 or 2:"))
if a==1:
    start= eval(input("enter the starting number range:"))
    end=eval(input("enter the ending number range:"))
    for x in rnage(start,end):
        print(x,end="")
elif a==2:
    choice="y"
    value=0
    while (choice=="y"):
        print(value)
        value=value+1
        choice=input("press y to continue:")
else:
    print("NA")