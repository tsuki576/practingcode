import numpy    
a=numpy.array(["a","b","c","d"])
for value in a:
    print(value)

#2
a=1
n= int(input("Enter the upper limit for printing prime numbers:"))
while a<n:
    b=2
    while b<=(a/b):
        if not(a%b):
            break
        b=b+1
        if b>(a/b):
            print(a)
    a=a+1
print()
#3

for i in range(1,10):
  print(i)

a=0
y=int(input("Enter the last number of series:"))
for i in range (1,y+1):
  a=a+i
print(a)
#4
x=int(input("Enter the number of your choice:"))
ans=1
for i in range(1,x+1):
  ans=ans*i
print(ans)


