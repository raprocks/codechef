withdraw, balance = input().strip().split(" ")
withdraw, balance = int(withdraw), float(balance)

if withdraw % 5 == 0 and balance > withdraw+0.5:
    print(balance-withdraw-0.5)
else:
    print(balance)
