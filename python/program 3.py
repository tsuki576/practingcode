def sub_numbers():
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    sum_result=num1-num2
    print(f"the difference of {num1} and {num2} is: {sum_result}")
sub_numbers()

def div_numbers():
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    sum_result=num1/num2
    print(f"the remainder of {num1} and {num2} is: {sum_result}")
div_numbers()

def mul_numbers():
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    sum_result=num1*num2
    print(f"the product of {num1} and {num2} is: {sum_result}")
mul_numbers()

def bodmas_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the fourth number: "))
    sum_result = [(num3 * (num1 + num2)) / num4]
    print(f"The result of {num1} + {num2} * {num3} / {num4} is: {sum_result}")
bodmas_numbers()
