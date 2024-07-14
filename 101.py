def classify_quadrilateral(a, b, c, d):
    if a == b == c == d:
        return "Square"
    elif (a == c and b == d) or (a == b == d == c):
        return "Rectangle"
    elif (a == b == c) or (b == c == d) or (c == d == a) or (d == a == b):
        return "Rhombus"
    elif (a == c and b == d) or (a == b == d == c) or (a == b and c != d):
        return "Parallelogram"
    else:
        return "Quadrilateral"

side_lengths = (4, 4, 4, 4)  
type_of_quadrilateral = classify_quadrilateral(*side_lengths)
print(f"The quadrilateral with sides {side_lengths} is a {type_of_quadrilateral}")
