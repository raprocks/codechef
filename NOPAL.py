from itertools import cycle
from string import ascii_lowercase

alphabet_cycle = cycle(ascii_lowercase)

for _ in range(int(input().strip())):
    N = int(input().strip())
    for _ in range(N):
        print(next(alphabet_cycle), end="")
    print()
