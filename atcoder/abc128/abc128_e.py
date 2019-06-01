N, Q = [int(_) for _ in input().split()]
STX = [[int(_) for _ in input().split()] for i in range(N)]
D = [int(input()) for i in range(Q)]

from bisect import *

es = []

for s, t, x in STX:
    t1 = s - .5 - x
    t2 = t - .5 - x
    #print(t1, t2, x)
    es.append((t1, 1, x))
    es.append((t2, 0, x))

for d in D:
    es.append((d, 3, 0))

es.sort()

class MinGetSet:
    def __init__(self):
        self.values = set()
        self.min = None
    def getMin(self):
        if self.min is None:
            self.min = min(self.values) if self.values else None
        return self.min
    def add(self, v):
        self.values.add(v)
        if self.min is None or v < self.min:
            self.min = v
    def remove(self, v):
        self.values.remove(v)
        if self.min == v:
            self.min = None

s = MinGetSet()

for t, typ, x in es:
    if typ == 3:
        print(s.getMin() or -1)
    elif typ == 1:
        s.add(x)
    elif typ == 0:
        s.remove(x)
