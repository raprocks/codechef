test_cases = int(input())

for _ in range(test_cases):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().strip().split(' '))))
    sumArr = []
    for j in range(N-1, -1, -1):
        i = 0
        total = 0
        for k in range(j, N):
            total += matrix[i][k]
            i += 1
        sumArr.append(total)
    for i in range(N-1, -1, -1):
        j = 0
        total = 0
        for k in range(i, N):
            total += matrix[k][j]
            j += 1
        sumArr.append(total)
    print(max(sumArr))
