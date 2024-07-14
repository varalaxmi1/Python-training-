



def is_palindrome_number(number):
   
    num_str = str(number)
    
    
    if num_str == num_str[::-1]:
        return True
    else:
        return False


def main():
    try:
        
        number = int(input("Enter a number: "))
        
        
        if is_palindrome_number(number):
            print(f"{number} is a palindrome number.")
        else:
            print(f"{number} is not a palindrome number.")
    
    except ValueError:
        print("Please enter a valid integer number.")


if __name__ == "__main__":
    main()
