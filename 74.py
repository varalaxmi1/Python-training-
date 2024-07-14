
import math


def is_perfect_square(num):
    if num < 0:
        return False  
    root = math.isqrt(num)
    
    if root * root == num:
        return True
    else:
        return False


def main():
    try:
        
        number = int(input("Enter a number: "))
        
       
        if is_perfect_square(number):
            print(f"{number} is a perfect square.")
        else:
            print(f"{number} is not a perfect square.")
    
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()

