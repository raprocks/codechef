from itertools import cycle

for _ in range(int(input().strip())):
    N, K, X = map(int, input().strip().split())
    if K < X:
        print("-1")
        continue
    gol = cycle([i for i in range(K + 1) if i != X])
    for _ in range(N):
        print(next(gol), end=" ")
    print()
