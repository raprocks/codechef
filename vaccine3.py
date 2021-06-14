T = int(input())
for _ in range(T):
    input_arr = list(map(int, input().strip().split(' ')))
    G = input_arr[0]
    P = input_arr[1]
    X = input_arr[2:]
    minimum = 0
    maximum = 0
    i = 0 # day count
    groupcounter = 10
    totol = sum(X[(G-1):])
    ans = totol/P
    day = 0
    maxset = False
    minset = False
    rem = totol % P
    mind = totol // P if totol//P>0 else 1
    maxd = mind + 1 if rem >0 else mind
    print(mind, maxd)
