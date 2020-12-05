test_cases = int(input())

for _ in range(test_cases):
    count = 0
    A, B = map(int, input().strip().split())
    for x in range(1,A+1):
        for y in range(1,B+1):
            if (x+y)%2==0:
                count+= 1
    print(count)