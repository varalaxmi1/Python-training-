

def bitwise_xor_operation(num1, num2):
   
    result = num1 ^ num2
    
    
    print(f"Bitwise XOR Operation:")
    print(f"Operand 1 (Decimal): {num1}")
    print(f"Operand 1 (Binary): {bin(num1)}")
    print(f"Operand 2 (Decimal): {num2}")
    print(f"Operand 2 (Binary): {bin(num2)}")
    print(f"Bitwise XOR Result (Decimal): {result}")
    print(f"Bitwise XOR Result (Binary): {bin(result)}")


try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    
   
    bitwise_xor_operation(num1, num2)
except ValueError:
    print("Invalid input! Please enter valid integers.")
