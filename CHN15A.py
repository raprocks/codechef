test_cases = int(input())

for _ in range(test_cases):
    N, K = map(int, input().strip().split())
    initial = list(map(int, input().strip().split()))
    transmod = [i+K for i in initial]
    divisible = 0
    for each in transmod:
        if each % 7 == 0:
            divisible += 1
    print(divisible)
