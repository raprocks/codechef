test_cases = int(input())
matches_number = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for _ in range(test_cases):
    A, B = map(int, input().strip().split())
    total_matches = 0
    for i in str(A+B):
        total_matches += matches_number[int(i)]
    print(total_matches)
