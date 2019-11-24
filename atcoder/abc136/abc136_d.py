S = input()
N = len(S)

X = [0] * N

k = 0
for i in range(N - 1):
    if S[i + 1] == "L":
        if S[i] == "R":
            k = i + 1
        X[i + 1] = k

k = 0
for i in range(N - 1, -1, -1):
    if S[i] == "R":
        if S[i + 1] == "L":
            k = i + 1
        X[i] = k

result = [0] * N
for i in range(N):
    if (X[i] - i) % 2 == 0:
        result[X[i]] += 1
    else:
        result[X[i] - 1] += 1

print(*result)

