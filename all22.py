x = 10
y = 20
z = 30
a = 40
print("Logical OR with Multiple Boolean Expressions:")
expr1 = (x < y)
expr2 = (y > z)
expr3 = (z == a)
expr4 = (x != y)
result = expr1 or expr2 or expr3 or expr4
print(f"x < y: {expr1}")        
print(f"y > z: {expr2}")       
print(f"z == a: {expr3}")   
print(f"x != y: {expr4}")       
print(f"Result of (expr1 or expr2 or expr3 or expr4): {result}")

