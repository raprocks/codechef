from math import floor

for _ in range(int(input())):
    maxprof = 0
    for _ in range(int(input())):
        S, P, V = map(int, input().strip().split())
        if ((P//(S+1))*V) > maxprof:
            maxprof = ((P//(S+1))*V)
    print(maxprof)
