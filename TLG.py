test_cases = int(input())
lead = {"player": 0, "lead":0}
for _ in range(test_cases):
    score1, score2 = map(int, input().strip().split())
    score_diff = score1 - score2
    if score_diff < 0:
        if -(score_diff) > lead["lead"]:
            lead["player"] = 2
            lead["lead"] = -(score_diff)
        else:
            pass
    else:
        if score_diff > lead["lead"]:
            lead["player"] = 1
            lead['lead'] = (score_diff)
    print(lead)
print(lead['player'], lead['lead'])
