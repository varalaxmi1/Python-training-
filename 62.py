

def compare_string_lengths(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    
    if length1 > length2:
        return "The first string is longer."
    elif length1 < length2:
        return "The second string is longer."
    else:
        return "Both strings are of equal length."


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")


result = compare_string_lengths(str1, str2)
print(result)
