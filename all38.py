def left_shift_operation(num, shift_positions):
    
    result = num << shift_positions
    
    
    print(f"Left Shift Operation:")
    print(f"Operand (Decimal): {num}")
    print(f"Operand (Binary): {bin(num)}")
    print(f"Shift Positions: {shift_positions}")
    print(f"Result (Decimal): {result}")
    print(f"Result (Binary): {bin(result)}")


try:
    num = int(input("Enter an integer: "))
    shift_positions = 3  
   
    left_shift_operation(num, shift_positions)
except ValueError:
    print("Invalid input! Please enter a valid integer.")

