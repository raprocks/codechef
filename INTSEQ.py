from math import log


def mysol(inp: int):
    if inp & (inp - 1) != 0:
        return 1 if inp % 2 == 0 else 0
    return int(log(inp, 2))


def optimum(inp: int):
    count = 0
    while inp % 2 == 0:
        count += 1
        inp //= 2
    return count


if __name__ == "__main__":
    # for _ in range(int(input())):
    #     inp = int(input().strip())
    #     myres = mysol(inp)
    for i in range(1, 10**9):
        if optimum(i) != mysol(i):
            print(i, mysol(i), optimum(i))
            break
