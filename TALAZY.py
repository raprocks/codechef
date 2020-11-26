test_cases = int(input())

for _ in range(test_cases):
    assignments, break_time, time_for_each_assignment = map(
        int, input().strip().split())
    time = 0
    while assignments > 0:
        assignments_in_session = int(assignments/2) \
            if assignments % 2 == 0 else int((assignments+1)/2)
        time += assignments_in_session*time_for_each_assignment
        assignments -= assignments_in_session
        if assignments == 0:
            break
        time += break_time  # break
        time_for_each_assignment *= 2
    print(int(time))
