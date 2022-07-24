for _ in range(int(input().strip())):
    X, Y = map(int, input().strip().split())
    N = 0
    if X == Y:
        N = (X * 2) - 1
        print(N)
        continue
    N += Y * 2
    N += X - Y
    print(N)
