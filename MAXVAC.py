for _ in range(int(input().strip())):
    N, X = map(int, input().split())
    S = list(input())
    vacs = 0
    i = 0
    to_loop_till = N - X + 1
    while i < to_loop_till:
        split = S[i : i + X]
        if split.count("1"):
            i += 1
        else:
            vacs += 1
            S = S[:i] + S[i + X :]
            to_loop_till -= X
    i = 0
    while i < to_loop_till:
        if S[i : i + X].count("1") < 2:
            vacs += 1
            break
        i += 1

    print(vacs)
