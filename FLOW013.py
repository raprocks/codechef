test_cases = int(input())

for _ in range(test_cases):
    A, B, C = map(int, input().strip().split(' '))
    if A+B+C == 180:
        print("YES")
    else:
        print('NO')
