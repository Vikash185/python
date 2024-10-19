# Simple Calculator in Python

# Take user input
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
operator = input("Enter Operator (+, -, *, /, %): ")

# Perform operation based on the operator
if operator == '+':
    print(f"Addition of numbers is: {num1 + num2}")
elif operator == '-':
    print(f"Subtraction of numbers is: {num1 - num2}")
elif operator == '*':
    print(f"Multiplication of numbers is: {num1 * num2}")
elif operator == '/':
    # Handle division by zero case
    if num2 != 0:
        print(f"Division of numbers is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed")
elif operator == '%':
    print(f"Remainder is: {num1 % num2}")
else:
    print("Enter a valid operator")
