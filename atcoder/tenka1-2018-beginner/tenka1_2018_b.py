A, B, K = [int(_) for _ in input().split()]

while 1:
    if K == 0:
        break
    K -= 1
    A, B = A // 2, B + A // 2
    if K == 0:
        break
    K -= 1
    A, B = A + B // 2, B // 2

print(A, B)
