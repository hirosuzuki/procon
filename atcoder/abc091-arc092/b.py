N = int(input())
S = [input() for i in range(N)]
M = int(input())
T = [input() for i in range(M)]

c = {}
for s in S:
    c[s] = c.get(s, 0) + 1
for s in T:
    c[s] = c.get(s, 0) - 1

print(max(0, max(c.values())))
