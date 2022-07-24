from collections import deque

for _ in range(int(input().strip())):
    N = int(input())
    s = input()
    if N % 2 != 0:
        print("NO")
        continue
    half = N // 2
    con = False
    dict_string = {i: s.count(i) for i in set(s)}
    for i in dict_string.values():
        if i > N // 2:
            print("NO")
            con = True
            break
    if con:
        continue
    out = ""
    # print(dict_string)
    first_half = deque()
    second_half = deque()
    first = True
    for k, v in dict_string.items():
        while v > 0:
            if first:
                first_half.append(k)
                first = False
            else:
                second_half.append(k)
                first = True
            v -= 1
    mega_list = first_half + second_half
    changes = -1
    i = 0
    lim = N // 2
    while i < lim:
        if mega_list[i] == mega_list[N - 1 - i]:
            l
            print(
            changes -= 1
            i = 0
            continue
        i += 1
    print("YES")
    print("".join(mega_list))
