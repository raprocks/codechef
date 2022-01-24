for _ in range(int(input())):
    inp = input()
    if inp.startswith("</") and inp.endswith(">") and inp[2:-1].lower() == inp[2:-1] and inp[2:-1].isalnum():
        print("SUCCESS")
    else:
        print("ERROR")
