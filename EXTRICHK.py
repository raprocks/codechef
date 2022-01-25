sides = list(map(int, input().split()))
side_set = set(sides)
length_side_set = len(side_set)
if length_side_set == 1:
    print(1)
elif sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]:
    if length_side_set == 2:
        print(2)
    elif length_side_set == 3:
        print(3)
else:
    print(-1)
