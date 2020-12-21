import math

test_cases = int(input())

for _ in range(test_cases):
    inp = int(input())
    prime = True
    if inp == 1:
        print("no")
        continue
    elif inp == 2:
        print("yes")
        continue
    if inp % 2 == 0:
        print('no')
        continue
    for i in range(3, int(math.sqrt(inp))+1, 2):
        if inp % i == 0:
            prime = False
            break
        prime = True
    if prime:
        print('yes')
    else:
        print('no')
