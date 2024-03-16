Total=0
choice="yes"
while(choice=="yes"):
    Rate= int(input("enter the rate="))
    Quant= int(input("enter the quantity"))
    Total=(Rate*Quant)+Total
    choice=input("wish to contue-yes/no:")
print("your toal bill is:", Total)