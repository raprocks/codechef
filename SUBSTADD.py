for _ in range(int(input())):
    N, X, Y = map(int, input().split())
    A = map(int, input().split())
    B = map(int, input().split())
    impossible = False
    for a, b in zip(A, B):
        if b - a not in [X, Y]:
            print("NO")
            impossible = True
            break
    if not impossible:
        print("YES")
