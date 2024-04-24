import math

#calculates number of cans needed to paint a wall
def paint_calc(height, width, cover):
  num_cans = (height * width) / cover
  round_up_cans = math.ceil(num_cans)
  print(f"You'll need {round_up_cans} cans of paint.")

test_h = int(input("Height of wall (m) ")) # Height of wall (m)
test_w = int(input("Width of wall (m) ")) # Width of wall (m)
cover = 5
paint_calc(test_h, test_w, cover)