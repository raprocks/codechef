test_cases = int(input())


def mod(n):
    return -(n) if n < 0 else n


def prefixsumcount(arr):
    count = 0
    for i in range(len(arr)):
        if sum(arr[:i+1]) > 0:
            count += 1
    return count


for _ in range(test_cases):
    N, K = map(int, input().strip().split())
    if N == K:
        print(' '.join(map(str, range(1, N+1))))
        continue
    Nodd = N % 2 != 0
    Narr = []
    if Nodd:
        for i in range(1, N+1):
            if i % 2 != 0:
                Narr.append(i)
            else:
                Narr.append(-i)
    else:
        for i in range(1, N+1):
            if i % 2 == 0:
                Narr.append(i)
            else:
                Narr.append(-i)
    current_count = prefixsumcount(Narr)
    # print(prefixsumcount(Narr), K)
    if current_count == K:
        # print("equal")
        print(" ".join(map(str, Narr)))
    elif current_count < K:
        i = 0
        while prefixsumcount(Narr) < K:
            idx_to_change = -(2*i)-2
            # print(idx_to_change)
            if idx_to_change < -len(Narr):
                break
            Narr[idx_to_change] = mod(Narr[idx_to_change])
            i += 1
        print(" ".join(map(str, Narr)))
    elif current_count > K:
        i = 0
        while prefixsumcount(Narr) > K:
            idx_to_change = -(2*i)-1
            if idx_to_change < -len(Narr):
                break
            Narr[idx_to_change] = -(mod(Narr[idx_to_change]))
            i += 1
        print(" ".join(map(str, Narr)))
