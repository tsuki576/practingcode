up_L=eval(input("enter the upper limit for displaying prime numbers:"))
for value in range(2,up_L+1):
    is_prime=True
    for factor in range(2,value):
        if(value%factor==0):
            is_prime=False
            break
        if is_prime:
            print(value, end="")
    print()