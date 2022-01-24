for _ in range(int(input().strip())):
    C = int(input().strip())
    bin_c = bin(C)[2:]
    out_bin_A = ['1'] + ['0'] * (len(bin_c) - 1)
    out_bin_B = ['0'] * len(bin_c)
    for idx, bit in enumerate(bin_c[1:], 1):
        if bit == '0':
            out_bin_A[idx] = '1'
            out_bin_B[idx] = '1'
        elif bit == '1':
            out_bin_B[idx] = '1'
    print(int(''.join(out_bin_A), 2) * int(''.join(out_bin_B), 2))


# set bits in A,B to 1 if the bit in input is 0
# set most significant bit in A to 1
# set all other bits to 1 in B if the bit in C is 1
