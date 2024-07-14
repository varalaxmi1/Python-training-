


def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."


def main():
    try:
        
        number = float(input("Enter a number: "))
        
       
        result = check_number(number)
        print(result)
    
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
