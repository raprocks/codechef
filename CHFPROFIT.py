for _ in range(int(input().strip())):
    X, Y, Z = map(int, input().strip().split())
    print((X * Z) - (X * Y))
