try:
    base = float(input("Enter the base number: "))
    exponent = float(input("Enter the exponent: "))
    
    
    result = base ** exponent
    
   
    print(f"{base} raised to the power of {exponent} is {result}")
except ValueError:
    print("Invalid input! Please enter numerical values.")
