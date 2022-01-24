from math import ceil

for _ in range(int(input())):
    input_arr = list(map(int, input().strip().split(" ")))
    G = input_arr[0]
    P = input_arr[1]
    X = input_arr[G + 1 :]
    total_to_vaccinate = sum(X)
    min_to_vaccinate = sum(X[1:])
    min_days = ceil((min_to_vaccinate + 1) / P)
    max_days = ceil(total_to_vaccinate / P)
    print(min_days, max_days)
