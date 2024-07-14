num = int(input("Enter a number: "))

sum = 0
for i in range(1, num):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    sum += fact

if sum == num:
    print("The number is a strong number")
else:
    print("The number is not a strong number")
