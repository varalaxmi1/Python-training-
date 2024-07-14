a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))


if a + b > c and a + c > b and b + c > a:
    
    if a == b and b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("Right-angled triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a triangle")
