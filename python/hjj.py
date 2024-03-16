result= eval(input("enter the expr"))
print(result)
#2
x=5
if x==2:
    print("even")
elif x==3:
    print("odd")
else:
    print("wrong statement")
    #3 while loop
    i=5
while i>=1:
    print("hello",end="")
    i=i+1
    break
#4 for loop
x=["hello",67,90]
for i in x:
    print(i)
    #5 range 
    for i in range(12):
        if i>=1:
            print(i)
#6 break 
            av=5
            x=int(input("how many candies we have?"))
            i=1
            while i <=  x:
                if i>av:
                 print("bye")
                 break
                print("candy")
                i+=1
            print("out of stock")
#7 continue
    for i in range(1,101):
        if i&3==0:
            continue
        print(i)

print("bye")
# for else in 
nums=[10,29,38,50]
for num in nums:
    if num & 5==0:
        print(num)
        break
    

