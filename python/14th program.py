number=0
sum=0
print("enter numbers to add; negative number to end")
while True:
    number=eval(input("enter the number:"))
    if number<0:
        break
    sum+=number
print("the toatl is=",sum)