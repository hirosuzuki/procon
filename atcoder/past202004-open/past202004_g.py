Q = int(input())

l = []
ix = 0

from collections import defaultdict

for i in range(Q):
    xs = input().split()
    if xs[0] == "1":
        C, X = xs[1], int(xs[2])
        l.append([C, X])
        #print(l[ix:])
    elif xs[0] == "2":
        D = int(xs[1])
        cs = defaultdict(int)
        while D > 0 and ix < len(l):
            e = l[ix]
            if e[1] > D:
                cs[e[0]] += D
                e[1] -= D
                D = 0
            else:
                cs[e[0]] += e[1]
                D -= e[1]
                ix += 1
        s = sum(cs[k]**2 for k in cs)
        print(s)
        


