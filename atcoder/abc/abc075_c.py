class UnionFind():
    # https://qiita.com/hukuhuku11111a1/items/1bbf67d90630552eb512
    def __init__(self, size):
        self.table = [-1] * size

    def find(self, x):
        while 1:
            i = self.table[x]
            if i < 0:
                return x
            x = i

    def union(self,x,y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 == s2:
            return
        d = self.table[s1] - self.table[s2]
        if d < 0:
            self.table[s2] = s1
        elif d > 0:
            self.table[s1] = s2
        else:
            self.table[s1] += -1
            self.table[s2] = s1

N, M = [int(_) for _ in input().split()]
ab = [[int(_) for _ in input().split()] for _ in range(M)]

result = 0

for a1, b1 in ab:
    uf = UnionFind(N + 1)
    for a, b in ab:
        if (a, b) == (a1, b1):
            continue
        uf.union(a, b)
    rs = set([])
    for i in range(1, N + 1):
        rs.add(uf.find(i))
    if len(rs) > 1:
        result += 1

print(result)
    

