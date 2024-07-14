try:
    float_value = float(input("Enter a float number: "))
    int_value = int(input("Enter an integer to increment by: "))
    
    
    result = float_value + int_value
    
    
    print(f"The result of incrementing {float_value} by {int_value} is {result}")
except ValueError:
    print("Invalid input! Please enter a valid float number and an integer.")
