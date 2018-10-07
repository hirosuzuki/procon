import math

N, M = [int(_) for _ in input().split()]


sr = int(math.sqrt(M))

result = 1

for i in range(sr, 0, -1):
    if M % i == 0:
        r = i
        if M >= N * r:
            result = max(r, result)
        r = M // i
        if i >= N:
            result = max(r, result)

print(result)