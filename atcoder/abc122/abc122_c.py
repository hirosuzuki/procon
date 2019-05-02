N, Q = [int(_) for _ in input().split()]
S = input()
LR = [[int(_) for _ in input().split()] for i in range(Q)]

cs = [0] * N

r = 0
for i in range(1, N):
    if S[i-1:i+1] == "AC":
        r += 1
    cs[i] = r

for l, r in LR:
    result = cs[r - 1] - cs[l -1]
    print(result)

