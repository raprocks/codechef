import math
test_cases = int(input())
primes = []


def check_prime(n):
    global primes
    if n in primes:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


for _ in range(test_cases):
    x, y = map(int, input().strip().split())
    sum = x+y
    addr = 1
    found = False
    while not found:
        local_sum = sum+addr
        res = check_prime(local_sum)
        if res is True:
            found = True
            print(addr)
        else:
            addr += 1
