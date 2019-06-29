N = int(input())
P = [int(_) for _ in input().split()]

result = 0

for i in range(0, N - 2):
    if P[i] < P[i+1] < P[i+2] or P[i] > P[i+1] > P[i+2]:
        result += 1

print(result)
