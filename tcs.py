from tracemalloc import start


N = int(input())
s = list(input())
k = int(input()) - 1

start_type = bool(s[k - 1] not in "aeiou")


def is_consonant(char):
    return "C" if char not in "aeiou" else "V"


# can move in one direction only, if end of the string the direction of motion changes
# convert every character to consonant if is_consonant else to vowel

# move towards the end which is the nearest
# print(N - k, k)
direction = 1 if (N - 1 - k) < k else -1
# print(direction)
# consonants till end of string in direction
start_type = is_consonant(s[k])
change_to = "a" if start_type else "b"
# print(start_type)
end = N if direction == 1 else 0
cost = 0
last_idx = k
for i in range(k, end, direction):
    char = s[i]
    # print(char)
    if start_type == is_consonant(char):
        # print("cost increasing by ", 1 + abs(last - i))
        cost += 1 + abs(last_idx - i)
        # print("changing", char, "to", change_to)
        s[i] = change_to
        last_idx = i
        # print(s)
# change direction
direction *= -1
cursor_pos = end + direction
new_end = N if direction == 1 else 0
# now cursor is as end + direction
# iterate from end+direction to new_end

for i in range(cursor_pos, new_end + direction, direction):
    char = s[i]
    if start_type == is_consonant(char):
        # print("cost increasing by ", 1 + abs(last - i))
        cost += 1 + abs(last_idx - i)
        # print("changing", char, "to", change_to)
        s[i] = change_to
        last_idx = i
        # print(s)
print(cost)
