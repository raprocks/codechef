for _ in range(int(input())):
    N = int(input())
    bin_str = input()
    count_one = 0
    count_zero = 0
    for char in bin_str:
        if char == "0":
            count_zero += 1
        else:
            count_one += 1
    if N % 2 != 0:
        odd_ele = "0" if count_zero % 2 != 0 else "1"
        if odd_ele == "1":
            count_one -= 1
        else:
            count_zero -= 1
    if count_one % 2 == 0 and count_zero % 2 == 0:
        print("YES")
    elif count_zero == count_one:
        print("YES")
    else:
        print("NO")


"""
can be palindrome when
1. count of 1 and coutn of 0 is same
or
2. count of 0 and count of 1 is even
"""
