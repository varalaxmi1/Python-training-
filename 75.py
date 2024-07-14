

def find_greatest(num1, num2, num3):
   
    if num1 >= num2 and num1 >= num3:
        return num1
    
    elif num2 >= num1 and num2 >= num3:
        return num2
    
        return num3


def main():
    try:
       
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        number3 = float(input("Enter the third number: "))
        
       
        greatest = find_greatest(number1, number2, number3)
        print(f"The greatest number is: {greatest}")
    
    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
