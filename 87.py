num = int(input("Enter a number: "))

sum_of_digits = 0
for digit in str(num):
    sum_of_digits += int(digit)

if num % sum_of_digits == 0:
    print("The number is a Harshad number")
else:
    print("The number is not a Harshad number")
