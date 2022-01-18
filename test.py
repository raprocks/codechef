t = int(input())  # number of test cases
results = []
for _ in range(t):
    n, x = input().split()  # n is number of fds available, x is number of gold coins required
    num_of_fd, gold_coins = int(n), int(x)

    fds = input()  # amount of money in every fd
    fixed_deposits = [int(num) for num in fds.split()]

    if sum(fixed_deposits) < gold_coins:
        # not possible if total amount in fd is less than gold coins
        results.append(-1)
    elif fixed_deposits[0] >= gold_coins:
        # if fd1 is equal or greater then no further comparison required
        results.append(1)
    else:
        total = 0
        fixed_deposits.sort(reverse=True)
        for i in range(len(fixed_deposits)):
            total += fixed_deposits[i]
            if total >= gold_coins:
                results.append(i+1)
                break

for r in results:
    print(r)
