D1, V1, D2, V2, P = map(int, input().strip().split())
produced = 0
d = 0
while produced < P:
    d += 1
    if d >= D1:
        produced += V1
    if d >= D2:
        produced += V2
print(d)
