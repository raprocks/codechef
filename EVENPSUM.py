test_cases = int(input())


def oddnum(n):
    odd = False if n % 2 == 0 else False
    if odd:
        return n//2+1
    else:
        return n//2


for _ in range(test_cases):
    count = 0
    A, B = map(int, input().strip().split())
    oddA = oddnum(A)
    oddB = oddnum(B)
    count = (oddA*oddB)+((A-oddA)*(B-oddB))
    print(count)
