x=int(input("enter the number of items:"))
total=0
discount=0

for i in range(1, x+1):
    rate=eval(input("enter the rate:"))
    quantity=eval(input("enter the quantity:"))
    total=total+(rate*quantity)
print("grand total is:",total)

if total>999:
    discount=total*0.1
    print("you received a discount of 10%=",discount)
elif total>799:
    discount=total*00.8
    print("you received a discount of 8%=",discount)
elif total>599:
    discount=total*0.05
    print("you received a discount of 5%=",discount)
else:
    print("no discount received")
print("net amount is:",total-discount)
