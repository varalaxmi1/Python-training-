


def bitwise_not_operation(num):
   
    result = ~num
    
    
    print(f"Bitwise NOT Operation:")
    print(f"Operand (Decimal): {num}")
    print(f"Operand (Binary): {bin(num)}")
    print(f"Bitwise NOT Result (Decimal): {result}")
    print(f"Bitwise NOT Result (Binary): {bin(result)}")


try:
    num = int(input("Enter an integer: "))
    
    
    bitwise_not_operation(num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")

