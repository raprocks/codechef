test_cases = int(input())

for _ in range(test_cases):
    N, D = map(int, input().strip().split())
    agearr = map(int, input().strip().split())
    at_risk = 0
    not_at_risk = 0
    days = 0
    for i in agearr:
        if i <= 9 or i >= 80:
            at_risk += 1
        else:
            not_at_risk += 1
    while at_risk > 0:
        #    print("another day")
        days += 1
        at_risk -= D
    #   print("days passed", days, "atriskleft", at_risk)
    while not_at_risk > 0:

        #    print("another day")
        days += 1
        not_at_risk -= D
    #    print("days passed", days, "notatriskleft", not_at_risk)
    print(days)
