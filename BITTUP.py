T = int(input())
tenk9mod = 10**9 + 7
for _ in range(T):
    N, M = map(int, input().strip().split())
    bit0permut = pow(2, N) - 1
    NTuples = pow(bit0permut, M, tenk9mod)
    print(NTuples)
