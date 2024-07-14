
number = int(input())
if number < 0:
    print(f"{number} is not a perfect square")
else:
    
    root = int(number ** 0.5)
    
    
    if root * root == number:
        print(f"{number} is a perfect square")
    else:
        print(f"{number} is not a perfect square")
