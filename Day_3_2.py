"""
BMI 2.0
"""

# Enter your height in meters e.g., 1.55
height = float(input("Enter your height in meters. "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight in kilograms. "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height * height)
if bmi < 18.5:
  print(f"Your BMI is {round(bmi, 2)}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {round(bmi, 2)}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {round(bmi, 2)}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {round(bmi, 2)}, you are obese.")
else:
  print(f"Your BMI is {round(bmi, 2)}, you are clinivally obese.")