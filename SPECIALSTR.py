for _ in range(int(input())):
    N = int(input())
    s = input()
    M = int(input())
    a_idx = [i for i, x in enumerate(s) if x == "a"]
    if not a_idx:
        print(-1)
        continue
    if 0 not in a_idx:
        a_idx = [0] + a_idx

    for i in range(len(a_idx[1:])):
        if a_idx[i + 1] - a_idx[i] < M:
            continue
        chunk = s[a_idx[i - 1] : a_idx[i + 1]]
