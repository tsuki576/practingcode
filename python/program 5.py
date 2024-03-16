x=int(input("Enter the number of items:"))
total=0
discount=0

for i in range(1,x+1):
    rate=eval(input("Enter the rate(i):"))
    quantity=eval(input("Enter the quantity(i):"))
    total=total+(rate*quantity)
print("Grand total is:", total)

if total >999:
    discount=total*0.1
    print("You recieved a discount of 10% =", discount)
elif total>799:
    discount=total*0.08
    print("You recieved a discount of 8% =", discount)
elif total>599:
    discount=total*0.05
    print("You recieved a discount of 5% =", discount)
else:
    print("No discount recieved")
print("Net amount is",total-discount)
