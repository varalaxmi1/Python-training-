num = int(input("Enter a number: "))


digits = len(str(num))

sum_of_digits = sum(int(digit) ** digits for digit in str(num))


if num == sum_of_digits:
    print("The number is an Armstrong number")
elif num == sum(int(digit) for digit in str(num)):
    print("The number is a sum of its digits")
elif num == sum(int(digit) ** 2 for digit in str(num)):
    print("The number is a sum of the squares of its digits")
else:
    print("The number is not a special number")

