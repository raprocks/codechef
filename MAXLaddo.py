inp = int(input())
switch = True
solu = []
to_sub = 1
count = 0
while switch:
    solu.append(to_sub)
    inp -= to_sub
    to_sub += 1
    count += 1
    if solu[-1] > (inp - (solu[-1]+1)):
        solu.append(inp)
        count += 1
        switch = False
print(count)
print(" ".join(map(str, solu)))
