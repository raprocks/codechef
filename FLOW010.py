test_cases = int(input())

for _ in range(test_cases):
    inp = input().upper()
    if inp == "B":
        print("BattleShip")
    elif inp == "C":
        print("Cruiser")
    elif inp == "D":
        print("Destroyer")
    elif inp == "F":
        print("Frigate")
