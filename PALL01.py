test_cases = int(input())

for _ in range(test_cases):
    inp = input()
    if inp == inp[::-1]:
        print('wins')
    else:
        print('loses')
