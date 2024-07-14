a = 15.5
b = 20.0
c = 25.7
d = 10.1
print("Logical Operators with Floating-Point Numbers:")
expr1 = a > b
expr2 = c < d
expr3 = a <= b
expr4 = c >= d
result_and = (expr1 and expr3)  
result_or = (expr1 or expr2)     i
result_not = not expr4         
print(f"a > b: {expr1}")         
print(f"c < d: {expr2}")        
print(f"a <= b: {expr3}")       
print(f"c >= d: {expr4}")       
print(f"Result of (expr1 and expr3): {result_and}")
print(f"Result of (expr1 or expr2): {result_or}")
print(f"Result of not expr4: {result_not}")


