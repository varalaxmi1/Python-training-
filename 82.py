string1 = input("Enter first string: ")
string2 = input("Enter second string: ")


if len(string1) > len(string2):
    print("String1 is longer")
elif len(string1) < len(string2):
    print("String2 is longer")
else:
    print("Both strings are equal in length")
