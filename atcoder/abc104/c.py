D, G = [int(_) for _ in input().split()]
PC = [[int(_) for _ in input().split()] for i in range(D)]
P = [p for p, c in PC]
C = [c for p, c in PC]

from heapq import *

h = []

heappush(h, (0, 0, (0,)*D))

result = 0

ef = {}

while h:
    t, score, pat = heappop(h)
    # print(t, score, pat)
    if score >= G:
        result = t
        break

    def add(i, pat, d):
        pat1 = list(pat)
        if pat1[i] +d <= P[i]:
            pat1[i] += d
            pat1 = tuple(pat1)
            if not pat1 in ef:
                t1 = t + d
                score1 = score + (i+1)*100*d
                if pat1[i] == P[i]:
                    score1 += C[i]
                ef[pat1] = t
                heappush(h, (t1, score1, pat1))

    for i in range(D-1, -1, -1):
        if pat[i] < P[i]:
            add(i, pat, 1)
            break

    for i in range(D):
        if pat[i] + 1 < P[i]:
            add(i, pat, P[i] - pat[i])

print(result)
