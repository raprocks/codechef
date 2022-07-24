from math import log

for _ in range(int(input())):
    X, M = map(int, input().split())
    if M == 0:
        print(0)
        continue
    ops = M
    blocks = 1
    ops -= 1
    # print(ops, blocks, end=" - \n")
    if ops <= 0:
        print(blocks // X)
        continue
    max_shift = min(int(log(X, 2)), ops)
    blocks = blocks << max_shift
    ops -= max_shift
    # print(ops, blocks, end=" - \n")
    if ops <= 0:
        print(blocks // X)
        continue
    if blocks % X != 0:
        blocks = X + (blocks - (X - blocks))
        ops -= 1
        # print(ops, blocks, end=" -- \n")
    if ops <= 0:
        print(blocks // X)
        continue
    buildings = 1
    # print(ops, blocks, end=" - \n")
    print(buildings + ops)
    # print(blocks // X)
