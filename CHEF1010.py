for _ in range(int(input())):
    _ = input()
    binstr = input()
    one_count = binstr.count("1")
    zero_count = binstr.count("0")
    print(max(min(one_count, zero_count) - 1, 0))
