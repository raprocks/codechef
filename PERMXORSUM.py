from math import log

"""
5
1
2
3
4
29012022
"""
for _ in range(int(input())):
    N = int(input())
    if N == 0:
        print(0)
        continue
    nearest_even = N if N % 2 == 0 else N - 1
    nearest_lowest_2 = int(log(N, 2))
    print(f"{nearest_even=}, {nearest_lowest_2=}")
    # print(nearest_lowest_2)
    print("changebit: ", nearest_even - (2 ** nearest_lowest_2))
    tot = (nearest_even + 1) * (nearest_even - (2 ** nearest_lowest_2))
    print(tot)

"""
5 7 2 7 7
4 5 1 3 2
1 2 3 4 5
"""
"""
1 2 3 4 5
2 1 4 3 2
3 3 7 7 7
"""
