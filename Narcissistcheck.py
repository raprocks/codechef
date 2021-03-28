testcases = int(input().strip())

for _ in range(testcases):
    inp = input().strip().replace(' ', '')
    toraise = len(inp)
    total = 0
    for num in inp:
        total += int(num)**toraise
    if int(inp) == total:
        print("Yes")
    else:
        print("No")
