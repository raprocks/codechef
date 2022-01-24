import itertools
for _ in range(int(input().strip())):
    N = int(input().strip())
    if N % 2 == 0:
        print("NO")
    else:
        print("YES")
        for i in range(1, N+1, 2):
            print(i, end=" ")
        for i in range(N-1, 0, -2):
            print(i, end=" ")
        print()


# For a permutation P of length N, we define L(P) to be the length of the longest increasing subsequence in P. That is, L(P) is the largest integer K such that there exist indices i1<i2<…<iK such that Pi1<Pi2<…<PiK.

# Define PR to be the permutation (PN,PN−1,…,P1).

# You are given a positive integer N. You need to output a permutation P of length N such that L(P)=L(PR), or say that none exist.

# Note: P is said to be a permutation of length N if P is a sequence of length N consisting of N distinct integers between 1 and N. For example, (3,1,2) is a permutation of length 3, but (1,4,2), (2,2,3) and (2,1) are not.

# 1 YES [1]
# 2 NO
# 3 YES [2,3,1]
# 4 NO [1,2,3,4] [1,3,4,2]
# 5 YES [1,3,5,4,2]
