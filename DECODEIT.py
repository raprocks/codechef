test_cases = int(input())
lis = ["abcdefghijklmnop"]
dec = {}
dec = {
    "0": {"0": {"0": {"0": 'a',
                      "1": 'b'},
                "1": {"0": 'c',
                      "1": 'd'}},
          "1": {"0": {"0": 'e',
                      "1": 'f'},
                "1": {"0": 'g',
                      "1": 'h'}}},
    "1": {"0": {"0": {"0": 'i',
                      "1": 'j'},
                "1": {"0": 'k',
                      "1": 'l'}},
          "1": {"0": {"0": 'm',
                      "1": 'n'},
                "1": {"0": 'o',
                      "1": 'p'}}
          }
}

for _ in range(test_cases):
    decoded = ""
    N = int(input())
    inp = input()
    for i in range(N//4):
        c = inp[i*4:(i+1)*4]
        decoded += dec[c[0]][c[1]][c[2]][c[3]]
    print(decoded)
