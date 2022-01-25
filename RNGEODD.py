L, R = map(int, input().strip().split())
print(" ".join(map(str, range(L, R + 1, 2) if L % 2 != 0 else range(L + 1, R + 1, 2))))
