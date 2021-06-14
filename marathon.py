T = int(input())


def marathon():
    D, d, A, B, C = map(int, input().strip().split(" "))


    total = d*D


    if total >= 42:
        print(C)
    elif total >= 21:
        print(B)
    elif total >= 10:
        print(A)
    else:
        print(0)

for _ in range(T):
    marathon()
