test_cases = int(input())

"cakewalk"
"simple"
"easy"
"easy-medium"
"medium"
"medium-hard"
"hard"

for _ in range(test_cases):
    problems = int(input())
    difficulties = []
    for _ in range(problems):
        difficulty = input()
        difficulties.append(difficulty)
    if ("cakewalk" in difficulties) \
            and ("simple" in difficulties) \
            and ("easy" in difficulties) \
            and ("easy-medium" in difficulties or "medium" in difficulties) \
            and ("medium-hard" in difficulties or "hard" in difficulties):
        print("Yes")
    else:
        print("No")
