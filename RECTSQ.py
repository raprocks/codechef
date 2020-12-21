from math import gcd

test_cases = int(input())

for _ in range(test_cases):
    L, B = map(int, input().strip().split(' '))
    divisor = gcd(L, B)
    while divisor != 1:
        L //= divisor
        B //= divisor
        divisor = gcd(L, B)
    print(L*B)
