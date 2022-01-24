for _ in range(int(input())):
    N = int(input())
    A = list(sorted(map(int, input().strip().split())))
    mean_P = sum(A[: N - 1]) / (N - 1)
    mean_Q = A[N - 1]
    print(f"{mean_P + mean_Q:.6f}")
