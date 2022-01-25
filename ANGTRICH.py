# check if angle A, B, C can form a triangle
# print yes if possible else print No
angles = list(map(int, input().strip().split(" ")))
if (angles[0] + angles[1] + angles[2]) == 180 and 0 not in angles:
    print("YES")
else:
    print("NO")
