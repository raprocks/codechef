test_cases = int(input())

for _ in range(test_cases):
    inp = int(input())
    if inp < 1500:
        gross = inp+(0.1*inp)+(0.9 * inp)
        print(gross)
    else:
        gross = inp + 500 + (0.98*inp)
        print(gross)
