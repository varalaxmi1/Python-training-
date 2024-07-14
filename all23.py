age = 25
income = 30000
has_driver_license = True
is_student = False
print("Logical OR with Multiple Boolean Expressions:")
expr1 = (age < 18)
expr2 = (income > 50000)
expr3 = has_driver_license
expr4 = is_student
result = expr1 or expr2 or expr3 or expr4
print(f"Age < 18: {expr1}")                
print(f"Income > 50000: {expr2}")         
print(f"Has a driver license: {expr3}")  
print(f"Is a student: {expr4}")           
print(f"Result of (expr1 or expr2 or expr3 or expr4): {result}")

