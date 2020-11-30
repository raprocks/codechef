test_cases = int(input())
denominations = [50, 10, 5, 2, 1]

for _ in range(test_cases):
    moni = int(input())
    notes = 0
    notes += moni // 100
    change = moni % 100
    for denomination in denominations:
        notes += change // denomination
        change = change % denomination
        if change == 0:
            break
    print(notes)
