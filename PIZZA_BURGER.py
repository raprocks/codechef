for _ in range(int(input().strip())):
    X, Y, Z = list(map(int, input().strip().split()))
    if X < Y and X < Z:
        print("NOTHING")
    elif X >= Y:
        print("PIZZA")
    else:
        print("BURGER")
