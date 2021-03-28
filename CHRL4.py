N, K = map(int, input().strip().split(' '))


def check(a, b, k):
    return 1 <= b-a <= k


specials = list(map(int, input().strip().split(' ')))
