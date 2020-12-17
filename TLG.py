test_cases = int(input())
score1 = []
score2 = []
for _ in range(test_cases):
    a, b = map(int, input().strip().split())
    score1.append(a)
    score2.append(b)
lead_arr = []
for i in range(1, len(score1)+1):
    lead_arr.append(sum(score1[:i]) - sum(score2[:i]))
lead = max(lead_arr, key=lambda x: abs(x))
if lead >= 0:
    player = 1
else:
    player = 2
print(player, abs(lead))
