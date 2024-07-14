


def add_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def main():
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    
   
    choice = input("Enter 1 for addition or 2 for subtraction: ")

   
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
       
        if choice == '1':
            result = add_numbers(number1, number2)
            print(f"The result of addition is: {result}")
        elif choice == '2':
            result = subtract_numbers(number1, number2)
            print(f"The result of subtraction is: {result}")
        else:
            print("Invalid choice. Please enter 1 for addition or 2 for subtraction.")
            
    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
