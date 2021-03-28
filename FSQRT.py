test_cases: int= int(input())
import math

for _ in range(test_cases):
    inp = int(input())
    sqrt = math.sqrt(inp)
    sqrt = round(sqrt)
    print(sqrt)
    