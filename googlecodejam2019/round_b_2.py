T, W = [int(_) for _ in input().split()]

M = 2 ** 63

import sys

for i in range(1, T + 1):
    print(40)
    sys.stdout.flush()
    a40 = int(input())
    print(190)
    sys.stdout.flush()
    a190 = int(input())
    R = [0] * 6
    R[5] = a190 // 2147483648 % 128
    R[4] = a190 // 274877906944 % 128
    R[3] = a190 // 140737488355328 % 128
    a = (a40 - R[3] * 1024 - R[4] * 256 - R[5] * 64) % M
    R[2] = a // 8192 % 128
    R[1] = a // 1048576 % 128
    R[0] = a // 1099511627776 % 128
    print(*R)
    sys.stdout.flush()

    verdict = int(input())
