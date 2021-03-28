test_cases = int(input())

for _ in range(test_cases):
    inp = input()
    total = 0
    for i in inp:
        total += int(i)
    print(total)
