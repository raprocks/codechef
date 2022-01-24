for _ in range(int(input().strip())):
    A, B = map(int, input().split())
    if A < B:
        print("<")
    elif A > B:
        print(">")
    else:
        print("=")
