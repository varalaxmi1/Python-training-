def is_palindrome_number(num):
    # Convert number to string
    num_str = str(num)
    
    left = 0
    right = len(num_str) - 1
    
   
    while left < right:
        # Check if characters at both pointers are equal
        if num_str[left] != num_str[right]:
            return False
        
        # Move pointers towards the center
        left += 1
        right -= 1
    
    # If the loop completes without returning False, it's a palindrome
    return True

# Example usage
number = 12321

if is_palindrome_number(number):
    print(f"{number} is a palindrome number")
else:
    print(f"{number} is not a palindrome number")
