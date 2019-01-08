N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(M)]

R = [0] * (N + 1)

for a, b in AB:
    R[a] += 1
    R[b] += 1

for i in range(1, N + 1):
    print(R[i])
