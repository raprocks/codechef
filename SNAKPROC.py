test_cases = int(input())

for _ in range(test_cases):
    length = int(input())
    inp = input().replace('.', '')
    valid = True
    if inp.startswith('T') or \
            inp.endswith('H') or \
            (inp.count('H') != inp.count('T')):
        print('Invalid')
        continue
    for i in range(0, len(inp), 2):
        if inp[i] != 'H':
            valid = False
            break
    if valid:
        print('Valid')
    else:
        print('Invalid')
