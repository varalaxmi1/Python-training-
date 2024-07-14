




def check_even_odd(number):
    
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."


def main():
    try:
        
        number = int(input("Enter a number: "))
        
        
        result = check_even_odd(number)
        print(result)
    
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
