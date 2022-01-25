N = int(input().strip())
for i in range(N):
    if i % 2 == 0:
        start = (5 * i) + 1
        end = start + 4
        print(" ".join(map(str, range(start, end + 1))))
    else:
        start = (5 * i) + 5
        end = start - 4
        print(" ".join(map(str, range(start, end - 1, -1))))
