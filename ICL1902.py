# FlatLand
from math import sqrt
test_cases = int(input())

for _ in range(test_cases):
    remaining_circles = int(input())
    circles = 0
    while remaining_circles > 0:
        if remaining_circles == 1:
            circles += 1
            break
        elif remaining_circles == 0:
            break
        else:
            closest_square = int(sqrt(remaining_circles))
            circles += 1
            remaining_circles -= closest_square**2
    print(circles)
