D1, V1, D2, V2, P = map(int, input().strip().split())
# print(D1, V1, D2, V2, P)
d = 0
d += D1-1 if D1 < D2 else D2-1
# print("days wasted", d)
if D1 > D2:
    # print("d1 greater")
    timediff = D1 - D2
    # print(" tiemdiff ", timediff)
    prod_in_diff = timediff*V2
    # print(" production in diff ", prod_in_diff)
    P -= prod_in_diff
    # print("left to prod", P)
    d += timediff
    # print("time passed", d)
elif D2 > D1:
    # print("d2 greater")
    timediff = D2 - D1
    # print(timediff)
    prod_in_diff = timediff*V1
    # print(" tiemdiff ", timediff)
    P -= prod_in_diff
    # print("left to prod", P)
    d += timediff
    # print("time passed", d)
else:  # equal
    pass

prodspeed = V1 + V2
# print("both manu start, prodspedd now ", prodspeed)
while P > 0:
    # print("another day")
    P -= prodspeed
    d += 1
    # print("prod left", P, "days passed ", d)

print(d)
