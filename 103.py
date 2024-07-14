def is_composite_number(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not composite numbers
    
    # Check for factors other than 1 and itself
    for i in range(2, n):
        if n % i == 0:
            return True
    
    return False

# Example usage
number = 10

if is_composite_number(number):
    print(f"{number} is a composite number")
else:
    print(f"{number} is not a composite number")
