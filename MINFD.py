for _ in range(int(input())):
    N, X = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    # only possible if the sum of the fds exceed the requirement
    possible = bool(sum(A) >= X)
    if not possible:
        print(-1)
        continue
    A.sort()  # sort the fds by values
    count = 0
    total = 0
    while total < X:  # repeat until the total of popped fds is less than the requirement
        to_add = A.pop()  # pop the last fd which should be the largest yet because of the sort
        total += to_add
        count += 1
    print(count)
