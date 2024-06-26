"""
BMI 2.0
"""

# Enter your height in meters e.g., 1.55
height = float(input("Enter your height in meters. "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight in kilograms. "))
bmi = weight / (height * height) * 10000
if bmi < 18.5:
  print(f"Your BMI is {round(bmi)}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {round(bmi)}, you are obese.")
else:
  print(f"Your BMI is {round(bmi)}, you are clinically obese.")