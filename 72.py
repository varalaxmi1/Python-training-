
def is_perfect_number(num):
    if num <= 1:
        return False
    
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
   return sum_of_divisors == num

def is_even(num):
    return num % 2 == 0


def main():
    try:
       
        number = int(input("Enter a number: "))
        
       
        if is_even(number):
            if is_perfect_number(number):
                print(f"{number} is an even perfect number.")
            else:
                print(f"{number} is even but not a perfect number.")
        else:
            print(f"{number} is not even.")
    
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
