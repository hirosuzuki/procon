N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(M)]

rs = [0]
t = 0

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
        global t
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 == s2:
            rs.append(t)
            return
        x1, y1 = self.table[s1], self.table[s2]
        if x1 <= y1:
            x2 = x1 + y1
            self.table[s1] = x2
            self.table[s2] = s1
            t = t - (-x1*(-x1-1)//2) - (-y1*(-y1-1)//2) + (-x2*(-x2-1)//2)
        else:
            y2 = y1 + x1
            self.table[s2] = y2
            self.table[s1] = s2
            t = t - (-x1*(-x1-1)//2) - (-y1*(-y1-1)//2) + (-y2*(-y2-1)//2)
        rs.append(t)

uf = UnionFind(N + 1)
#print(uf.table)

for a,b in AB[::-1]:
    uf.union(a, b)
    #print(uf.table)

#print(rs)

tt = N*(N-1)//2
for r in rs[-2::-1]:
    print(tt - r)
