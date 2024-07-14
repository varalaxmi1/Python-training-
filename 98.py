score = float(input("Enter the score: "))  
grade = 'F' 
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'

# Print the grade
print(f"The grade for score {score} is {grade}")
