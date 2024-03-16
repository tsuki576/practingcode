i=1
n=int(input("enter the upper limiting of prime numbers"))
while(i<n):
    j=2
    while(j<=(i/j)):
        if not(i%j):
            break
        j=j+1
        if (j>(i/j)):
            print(i,end="")
    i=i+1
print()