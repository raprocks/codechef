A, B, C = map(int, input().strip().split())

s = (A + B + C) / 2
if s * (s - A) * (s - B) * (s - C) > 0:
    print("YES")
else:
    print("NO")
