
num1 = float(input("Enter the first number: "))  
num2 = float(input("Enter the second number: "))  # Change this to test different numbers
operation = input("Enter the operation (+, -, *, /): ")  # Change this to test different operations

# Perform the calculation based on the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"

# Print the result
print(f"The result of {num1} {operation} {num2} is {result}")
