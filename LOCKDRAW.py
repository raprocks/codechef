for _ in range(int(input().strip())):
    A, B, C = map(int, input().strip().split())
    if A + B == C or A + C == B or B + C == A:
        print("YES")
    else:
        print("NO")
