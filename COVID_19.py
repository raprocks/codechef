for _ in range(int(input())):
    N, M = map(int, input().strip().split())
    # for each pair a empty row
    rows_seatable = (N // 2) if (N % 2 == 0) else ((N // 2) + 1)
    seats_per_row = (M // 2) if (M % 2 == 0) else ((M // 2) + 1)
    print(rows_seatable*seats_per_row)
