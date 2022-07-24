for _ in range(int(input())):
    N = int(input())
    x = set()
    y = set()
    for _ in range(N):
        X, Y = map(int, input().split())
        x.add(X)
        y.add(Y)
    print(len(x) + len(y))
