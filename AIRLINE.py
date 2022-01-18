for _ in range(int(input())):
    A, B, C, D, E = map(int, input().strip().split())
    possible = bool(A+B+C <= D+E)
    if not possible:
        print("NO")
        continue
    bags = [A, B, C]
    carrieable_candidates = [x for x in bags if x <= E]
    if not carrieable_candidates:
        print("NO")
        continue
    max_carriable = max(carrieable_candidates)
    max_carriable = bags.remove(max_carriable)
    if sum(bags) <= D:
        print("YES")
    else:
        print("NO")
