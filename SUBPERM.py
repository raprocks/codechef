for _ in range(int(input())):
    N, K = map(int, input().split())
    if N == 1 and K == 1:
        print(1)
        continue
    if N > K and K == 1:
        print(-1)
        continue
    # print("start", end="  ")
    for i in range(1, K):
        print(i, end=" ")
    # print("flipped", end="  ")
    for i in range(N, K - 1, -1):
        print(i, end=" ")
    print("")