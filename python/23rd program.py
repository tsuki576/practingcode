print("please enter four numbers:")
sum=0
mylist=[]
for i in range (0,4):
    num=eval(input("enter number"+str(i+1)+":"))
    mylist+=[num]
    sum+=num
print("the number entered are:")
for x in mylist:
    print(x,end="")
print()
print("the sum of numbers is:",sum)
