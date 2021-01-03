test_cases = int(input())

for _ in range(test_cases):
    _, K, D = map(int, input().strip().split())
    total = sum(map(int, input().strip().split()))
    counter = total//K
    if counter >= D:
        print(D)
    else:
        print(counter)
