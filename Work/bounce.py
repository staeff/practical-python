# bounce.py
#
# Exercise 1.5
height = 100
counter = 0

while counter < 10:
    counter += 1
    height -= height*(2/5)
    print(counter, round(height, 4))
