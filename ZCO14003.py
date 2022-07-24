prices = []
N = int(input())
for _ in range(N):
    prices.append(int(input()))
prices.sort()
# [14, 20, 30, 53]


def rev_idx(idx):
    return prices[idx] * (N - idx)


max_rev = 0
for i in range(N):
    max_rev = max(max_rev, rev_idx(i))
print(max_rev)
