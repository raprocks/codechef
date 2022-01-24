for _ in range(int(input())):
    s0, s1, s2 = map(int, input().strip().split())
    sets = s0
    if s1 > s2:
        sets += s2
        s1 -= s2
        s2 = 0
        sets += s1 // 3
    elif s2 > s1:
        sets += s1
        s2 -= s1
        s1 = 0
        sets += s2 // 3
    else:
        sets += s2
        s1 = 0
        s2 = 0
    print(sets)
