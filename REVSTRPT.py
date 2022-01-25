N = int(input().strip())
for i in range(1, N+1):
    string = " "*(N-i) + "*"*i
    print(string)