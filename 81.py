assignment_score = float(input("Enter assignment score (out of 100): "))
exam_score = float(input("Enter exam score (out of 100): "))
project_score = float(input("Enter project score (out of 100): "))

overall_score = (assignment_score + exam_score + project_score) / 3


if overall_score >= 90:
    grade = "A"
elif overall_score >= 80:
    grade = "B"
elif overall_score >= 70:
    grade = "C"
elif overall_score >= 60:
    grade = "D"
else:
    grade = "F"


print("Grade:", grade)
