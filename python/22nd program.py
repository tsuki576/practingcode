print("please enter four numbers:")
n1=int(input("enter number 1:"))
n2=int(input("enter number 2:"))
n3=int(input("enter number 3:"))
n4=int(input("enter number 4:"))
sum=n1+n2+n3+n4
print("the sum of numbers",n1,n2,n3,n4,"is",sum)

#same type different method

print("please enter four numbers:")
sum=0
for i in range (0,4):
    num=eval(input("enter number"+str(i+1)+":"))
    sum+=num
print("the sum of numbers is:",sum)