'''
    SIMPLE CALCULATOR USING PYTHON
# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE
'''
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")

operation = input()


if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    #validation
    if(num1.isnumeric() and num2.isnumeric()):
        sum = int(num1) + int(num2)
        print("The sum of 2 numbers is :"+str(sum))
    else:
        print("Type a valid number please!")
elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    if(num1.isnumeric() and num2.isnumeric()):
        diff = int(num1) - int(num2)
        print("The difference of 2 numbers is:"+str(diff))
    else:
        print("Type a valid number please!")
elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    if(num1.isnumeric() and num2.isnumeric()):
        product = int(num1) * int(num2)
        print("The product of 2 numbers is:"+str(product))
    else:
        print("Type a valid number please!")
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    if(num1.isnumeric() and num2.isnumeric()):
        quotient = int(num1) / int(num2)
        print("The quotient of 2 numbers is:"+str(quotient))
    else:
        print("Type a valid number please!")
else:
    print("Please enter the valid operation")