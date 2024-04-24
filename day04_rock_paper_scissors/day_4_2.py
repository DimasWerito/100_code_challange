"""
Random Name
"""
import random

#input names separating them by comma and space
names_string = input("Who is having a dinner?\n")
# The code above converts the input into an array seperating
names = names_string.split(", ")
choice = random.randint(1, len(names)) - 1
chosen_name = names[choice]
print(f"{chosen_name} is going to buy the meal today!")