'''Contest Code:JAN222C Problem Code:EXAMTIME'''

for _ in range(int(input())):
    drag = list(map(int, input().strip().split()))
    sloth = list(map(int, input().strip().split()))

    if sum(drag) > sum(sloth):
        print("DRAGON")
    elif sum(drag) < sum(sloth):
        print("SLOTH")
    elif drag[0] > sloth[0]:
        print("DRAGON")
    elif drag[0] < sloth[0]:
        print("SLOTH")
    elif drag[1] > sloth[1]:
        print("DRAGON")
    elif drag[1] < sloth[1]:
        print("SLOTH")
    elif drag[2] > sloth[2]:
        print("DRAGON")
    elif drag[2] < sloth[2]:
        print("SLOTH")
    else:
        print("TIE")
