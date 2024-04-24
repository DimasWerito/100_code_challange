"""
найбільший спільний дільник
"""


first = int(input("Input the first number>>>"))
second = int(input("Input the second number>>>"))

gcd = min(first, second)

while not (first % gcd == 0 and second % gcd == 0):
    gcd -= 1

print(gcd)