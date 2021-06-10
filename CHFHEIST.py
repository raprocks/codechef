T = int(input())

for _ in range(T):
    D, d, P, Q = map(int, input().strip().split())
    totalparts = D//d
    leftdays = D%d
    partialhold = d* totalparts * (2*P + (totalparts -1)*Q)
    partialhold //=2
    lefthold = leftdays * (P + totalparts*Q)
    print(partialhold + lefthold)
