N = int(input())
A = [int(input()) for i in range(N)]

from collections import Counter

cs = Counter(A)
vs = dict((v, i) for i, v in enumerate(sorted(cs.keys())))

for a in A:
    print(vs[a])
