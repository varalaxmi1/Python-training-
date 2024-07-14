age = 25
height_cm = 170
weight_kg = 70
salary = 50000
print("Logical AND with Multiple Comparisons:")
age_check = (age >= 18) and (age <= 30)
height_check = height_cm >= 160
weight_check = (weight_kg >= 50) and (weight_kg <= 80)
salary_check = salary > 40000
final_result = age_check and height_check and weight_check and salary_check
print(f"Age between 18 and 30: {age_check}")
print(f"Height at least 160 cm: {height_check}")
print(f"Weight between 50 and 80 kg: {weight_check}")
print(f"Salary greater than 40000: {salary_check}")
print(f"Final result of all comparisons using AND: {final_result}")




