test_cases = int(input())

for _ in range(test_cases):
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    counter = 0
    max_limit = N*M
    A.sort()
    B.sort(reverse=True)
    idxA = 0
    idxB = 0
    sumA = sum(A)
    sumB = sum(B)
    while sumA <= sumB:
        counter += 1
        if idxA >= N or idxB >= M:
            A.sort()
            idxA = 0
            B.sort(reverse=True)
            idxB = 0

        A[idxA], B[idxB] = B[idxB], A[idxA]
        idxA += 1
        idxB -= 1
        sumA = sum(A)
        sumB = sum(B)
        if counter > max_limit or sumA > sumB:
            break
    if sumA > sumB:
        print(counter)
    else:
        print(-1)
