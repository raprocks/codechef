T = int(input())

def optimumtime(a,b):
    if a == -1:
        return b
    elif b == -1:
        return a
    return min(a,b)

for _ in range(T):
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    A1 = []
    A2 = []
    count1 = -1
    count2 = -1
    for i in range(N):
        cur = A[i]
        revcur = A[N-1-i]
        if cur == 1:
            count1 = 0
        if revcur == 2:
            count2 = 0
        A1.append(count1)
        A2.append(count2)
        if count1 != -1:
            count1 += 1
        if count2 != -1:
            count2 += 1
    A2.reverse()


    for idx, passenger in enumerate(B):
        if passenger == 1:
            print("0", end=" ")
            continue

        desttime = optimumtime(A1[passenger-1], A2[passenger-1])
        print(desttime, end=" ")
    print()
