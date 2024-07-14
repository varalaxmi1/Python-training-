
def check_sum_even_odd(num1, num2):
    total = num1 + num2
    if total % 2 == 0:
        return "The sum is even."
    else:
        return "The sum is odd."


try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    
    
    result = check_sum_even_odd(number1, number2)
    print(result)

except ValueError:
    print("Please enter valid integer numbers.")
