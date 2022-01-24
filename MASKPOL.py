for _ in range(int(input().strip())):
    N, A = map(int, input().strip().split())
    print(min(N - A, A))
