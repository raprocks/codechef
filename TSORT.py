length_of_array = int(input())
array = []
for _ in range(length_of_array):
    array.append(int(input()))
print('\n'.join(map(str, sorted(array))))
