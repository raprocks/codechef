for _ in range(int(input().strip())):
    a, b, c = map(int, input().strip().split())
    if a > 50:
        print("A")
    elif b > 50:
        print("B")
    elif c > 50:
        print("C")
    else:
        print("NOTA")
