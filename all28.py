age = 25
height_cm = 170
weight_kg = 70
salary = 50000
print("Logical NOT with Multiple Comparisons:")
age_check = not (age >= 18 and age <= 30)
height_check = not (height_cm >= 160)
weight_check = not (weight_kg >= 50 and weight_kg <= 80)
salary_check = not (salary > 40000)
final_result = age_check or height_check or weight_check or salary_check
print(f"Age is not between 18 and 30: {age_check}")
print(f"Height is less than 160 cm: {height_check}")
print(f"Weight is not between 50 and 80 kg: {weight_check}")
print(f"Salary is not greater than 40000: {salary_check}")
print(f"Final result of all NOT-ed comparisons using OR: {final_result}")




