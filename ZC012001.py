# nesting depth
# first position that achieves the nesting depth
# length of the maximum sequence between matching brackets
# the first position where such a maximum length sequence occurs.

length = input()

encoded = input()
encoded = "1 2 1 1 2 2 1 2 1 1 2 1 2 2 1 1 2 1 2 2"
"()(())()(()())(()())"
"2 4 6 9"

decoded = encoded.strip().replace(' ', '').replace('1', '(').replace('2', ')')
max_depth, max_depth_pos, max_length, max_length_pos = 0, 0, 0, 0
pos = 0
depth = 0
for each in decoded:
    pos += 1
    open_pos = 0
    local_open_pos = 0
    close_pos = 0
    local_close_pos = 0
    if each == "(":
        depth += 1

    elif each == ")":
        depth -= 1
    # nesting depth
    print(pos, depth)
    if max_length < (close_pos-open_pos+1):
        max_length = close_pos-open_pos+1


print(max_depth, max_depth_pos, max_length, max_depth_pos)
