

def compare_string_lengths(str1, str2):
   
    length1 = len(str1)
    length2 = len(str2)
    
    
    if length1 > length2:
        print("The first string is longer.")
    elif length1 < length2:
        print("The second string is longer.")
    else:
        print("Both strings are of equal length.")


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")


compare_string_lengths(str1, str2)
