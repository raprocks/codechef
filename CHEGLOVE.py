test_cases = int(input())

for _ in range(test_cases):
    fingers = int(input())
    finger_lengths = list(map(int, input().strip().split()))
    glove_lengths = list(map(int, input().strip().split()))
    front_zip = zip(finger_lengths, glove_lengths)
    back_zip = zip(finger_lengths, reversed(glove_lengths))
    front = True
    back = True
    for fing_len, glove_len in front_zip:
        if fing_len > glove_len:
            front = False
            break
    for fing_len, glove_len in back_zip:
        if fing_len > glove_len:
            back = False
            break

    if front and back:
        print("both")
    elif front and not back:
        print("front")
    elif back and not front:
        print("back")
    else:
        print("none")
