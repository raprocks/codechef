for _ in range(int(input())):
    a, b, c, p, q, r = map(int, input().split())
    if a + b + c > (p + q + r) / 2:
        print("Yes")
        continue
    diff_a = abs(p - a)
    diff_b = abs(q - b)
    diff_c = abs(r - c)
    max_diff = max(diff_a, diff_b, diff_c)
    if max_diff == diff_a:
        a = p
    elif max_diff == diff_b:
        b = q
    else:
        c = r
    if a + b + c > (p + q + r) / 2:
        print("Yes")
    else:
        print("No")

    da = p - a
    db = q - b
    dc = r - c
    if a + b + c > (p + q + r) / 2:
        print("YES")
        break
    elif da >= db or da >= dc:
        a = p
    elif db >= da or db >= dc:
        b = q
    elif dc >= db or dc >= da:
        c = r
    req_votes = (p + q + r) / 2
    total_votes = a + b + c
    if total_votes > req_votes:
        print("YES")
    else:
        print("NO")
