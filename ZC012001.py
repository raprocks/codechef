# nesting depth
# first position that achieves the nesting depth
# length of the maximum sequence between matching brackets
# the first position where such a maximum length sequence occurs.

length = input()

encoded = input()
# encoded = "1 2 1 1 2 2 1 2 1 1 2 1 2 2 1 1 2 1 2 2"
# "()(())()(()())(()())"
# "2 4 6 9"

decoded = encoded.strip().replace(' ', '').replace('1', '(').replace('2', ')')
max_depth, max_depth_pos, max_length, max_length_pos = 0, 0, 0, 0
pos = 0
depth = 0
open_pos = 0
last_zero_pos = 0
last_last_zero_pos = 0
local_open_pos = 0
close_pos = 0
local_close_pos = 0

for each in decoded:
    pos += 1
    if each == "(":
        depth += 1

    elif each == ")":
        depth -= 1
    # nesting depth
#    print(pos, depth)
    if depth > max_depth:
        max_depth_pos = pos
        max_depth = depth
#        print('max_depth_pos reset', max_depth_pos, "at depth:", depth)
    if depth == 0:
        last_last_zero_pos = last_zero_pos
        last_zero_pos = pos
#        print('zero_pos_reset', last_zero_pos,
#              "last_last_zero_pos", last_last_zero_pos)

    if (last_zero_pos - last_last_zero_pos) > max_length:
        max_length = (last_zero_pos - last_last_zero_pos)
        max_length_pos = last_last_zero_pos + 1
#        print("max_length detected starting at",
#              max_length_pos, "and max length is", max_length)


print(max_depth, max_depth_pos, max_length, max_length_pos)
