from collections import deque

for _ in range(int(input())):
    _ = input()
    A = deque(map(int, input().strip().split()))
    B = deque(map(int, input().strip().split()))
    C = []
    while len(A) != 0 and len(B) != 0:
        if A[0] < B[0]:
            A.append(B.popleft())
        else:
            B.append(A.popleft())
