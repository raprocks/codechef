def rohit():
    for _ in range(int(input())):
        N, K = map(int, input().strip().split(" "))
        s = list(input())
        odd_N = 0
        if N % 2 != 0:
            # s = s[: N // 2 + 1] + s[N // 2 :]
            odd_N = 1
        left = K
        for i in range(N // 2):
            # print(s[i], s[N - 1 - i])
            if s[i] == s[N - 1 - i]:
                continue
            else:
                left -= 1
        if left < 0:
            print("NO")
        else:
            if odd_N:
                print("YES")
            elif not odd_N and left % 2 == 0:
                print("YES")
            else:
                print("NO")


def aditi():
    def isPalindrome(s):
        return s[:n] == s[::-1]

    for _ in range(int(input())):
        (n, k) = map(int, input().split())
        input_str = input()
        s = [int(x) for x in input_str]

        if k == 0 and not isPalindrome(s):
            print("NO")
            break
        elif k == 0 and isPalindrome(s):
            print("YES")
            break

        cnt = 0
        j = n - 1
        if n % 2 == 1:
            r = n // 2 - 1
        else:
            r = n // 2
        for i in range(r):
            if cnt == k:
                break
            if s[i] != s[j]:
                s[i] = s[j]
                cnt += 1
            j = j - 1
        if isPalindrome(s) and cnt == k:
            print("YES")
        elif isPalindrome(s) and (k - cnt) > 0 and n % 2 == 1:
            print("YES")
        elif isPalindrome(s) and (k - cnt) % 2 == 0:
            print("YES")
        else:
            print("NO")


rohit()
