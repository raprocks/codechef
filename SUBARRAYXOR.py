from itertools import cycle

for _ in range(int(input())):
    N = int(input())
    first = True
    res = 0
    for _, i in zip(range(N), cycle([1, 2] if N % 2 else [1, 2, 3])):
        if first:
            res = i
            first = not first
        res = res ^ i
    print(res)
