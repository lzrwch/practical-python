# bounce.py
#
# Exercise 1.5

height = 100
number_jump = 0

while number_jump < 10:
    height *= 3/5
    number_jump += 1
    print(number_jump, round(height, ndigits=4))
