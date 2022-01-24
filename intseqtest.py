for _ in range(int(input())):
    k = int(input())
    b = 0
    while (k % 2 == 0):
        k /= 2
        b += 1
    print(b)
