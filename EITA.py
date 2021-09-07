for _ in range(int(input())):
    d,x,y,z = map(int, input().strip().split())
    one = 7*x
    two = d*y + (7-d)*z
    print(one) if one>two else print(two)
