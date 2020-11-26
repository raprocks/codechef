N, K = map(int, input().strip().split())
counter = 0
for _ in range(N):
    inp = int(input())
    counter += 1 if inp % K == 0 else 0
print(counter)
