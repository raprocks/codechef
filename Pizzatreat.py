test_cases = int(input())

for _ in range(test_cases):
    P = int(input())
    inp = map(int, input().strip().split()[1:])
    for cook in inp:
        while time_elapsed < 