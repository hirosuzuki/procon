import itertools
import collections

#N = int(input())
N = 4

ts = list(itertools.permutations(range(N)))

print(len(ts))

cs = collections.defaultdict(int)

for t in ts:
    p = set()
    for i, x in enumerate(t):
        p.add(x)
        p.add(x+1)
        if len(p) == N + 1:
            break
    if i == 3:
        pass
        #print(t, i)
    cs[i + 1] += 1

print(cs)

