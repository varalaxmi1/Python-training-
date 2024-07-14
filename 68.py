


def add_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def starts_with_vowel(s):
    
    if s and s[0].lower() in 'aeiou':
        return True
    else:
        return False


def main():
   
    string_input = input("Enter a string: ")
    
   
    if starts_with_vowel(string_input):
        print(f"The string starts with a vowel.")
    else:
        print(f"The string does not start with a vowel.")


if __name__ == "__main__":
    main()
