inp = int(input())


coins10 = inp // 10
inp = inp - (10*coins10)
coins5 = inp // 5
inp = inp - (5*coins5)
coins1 = inp
print(coins10 + coins5 + coins1)
