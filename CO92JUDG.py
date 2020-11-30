test_cases = int(input())

for _ in range(test_cases):
    _ = input()
    alice_time = list(map(int, input().strip().split()))
    bob_time = list(map(int, input().strip().split()))
    max_alice = max(alice_time)
    max_bob = max(bob_time)
    alice_time.remove(max_alice)
    bob_time.remove(max_bob)
    alice_total = sum(alice_time)
    bob_total = sum(bob_time)
    if alice_total < bob_total:
        print("Alice")
    elif bob_total < alice_total:
        print("Bob")
    else:
        print("Draw")
