for _ in range(int(input())):
    N = int(input())
    A = map(int, input().split())
    if N == 1:
        print(1)
        continue
    max_speed_cars = 0
    front_speed = 2 ** 32
    for a in A:
        if front_speed >= a:
            max_speed_cars += 1
        front_speed = min(a, front_speed)
    print(max_speed_cars)
