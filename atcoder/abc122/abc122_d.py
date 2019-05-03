N = int(input())
M = 10**9 + 7

E = "ACGT"

from collections import defaultdict

ngp = [
    "?AGC", "?GAC", "?ACG",
    "AGC?", "GAC?", "ACG?",
    "A?GC", "AG?C"
]

ng = set(["AGC", "GAC", "ACG"])

for x in ngp:
    for c in E:
        ng.add(x.replace("?", c))

rs = {"": 1}

for i in range(N):
    nrs = defaultdict(int)
    for k, v in rs.items():
        for e in E:
            nk = (k + e)[-4:]
            if not nk in ng:
                nrs[nk[-3:]] += v
    rs = nrs

result = sum(nrs.values()) % M

print(result)