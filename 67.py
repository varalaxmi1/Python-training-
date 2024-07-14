


def add_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def multiply_numbers(num1, num2):
    return num1 * num2


def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1 / num2


def main():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    
    choice = input("Enter the number corresponding to the operation (1/2/3/4): ")
    
    
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        
        if choice == '1':
            result = add_numbers(number1, number2)
            print(f"The result of addition is: {result}")
        elif choice == '2':
            result = subtract_numbers(number1, number2)
            print(f"The result of subtraction is: {result}")
        elif choice == '3':
            result = multiply_numbers(number1, number2)
            print(f"The result of multiplication is: {result}")
        elif choice == '4':
            result = divide_numbers(number1, number2)
            print(f"The result of division is: {result}")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            
    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
