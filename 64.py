
def compare_floats(num1, num2):
    if num1 > num2:
        return "The first number is greater than the second number."
    elif num1 < num2:
        return "The first number is less than the second number."
    else:
        return "Both numbers are equal."


try:
    number1 = float(input("Enter the first floating-point number: "))
    number2 = float(input("Enter the second floating-point number: "))
    
   
    result = compare_floats(number1, number2)
    print(result)

except ValueError:
    print("Please enter valid floating-point numbers.")
