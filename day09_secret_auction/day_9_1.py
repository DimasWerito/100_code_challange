"""
 GRADING PROGRAM
"""


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for name, score in student_scores.items():
  if score <= 70:
    student_grades[name] = "Fail"
  elif score <= 80:
    student_grades[name] = "Acceptable"
  elif score <= 90:
    student_grades[name] = "Exceeds Expectations"
  else:
    student_grades[name] = "Outstanding"

print(student_grades)