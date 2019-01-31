def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def primes(n):
    from math import sqrt
    p = [1] * (n + 1)
    for x in range(2, int(sqrt(n)) + 1):
        if p[x]:
            p[x * 2:n + 1:x] = [0] * ((n - x) // x)
    return (i for i in range(2, n + 1) if p[i])

p = list(primes(100))
print(len(p))

M = 10**9 + 7
L = 200000

Fm = {}
inverseFm = {}
x = 1
for i in range(L):
    Fm[i] = x
    x = x * (i + 1) % M

def inverseFm(x, cache={}):
    if x in cache:
        return cache[x]
    result = pow(Fm[x], M - 2, M)
    cache[x] = result
    return result

def C(n, r):
    result = Fm[n] * inverseFm(r) * inverseFm(n - r) % M
    return result
    
def solve():
    pass

if __name__ == '__main__':
    A = int(input())
    N, M = [int(_) for _ in input().split()]
    solve()

def Dijkstra(s, V, E):
    # https://ja.wikipedia.org/wiki/%E3%83%80%E3%82%A4%E3%82%AF%E3%82%B9%E3%83%88%E3%83%A9%E6%B3%95
    d = defaultdict(lambda:10**20)
    prev = defaultdict(lambda:None)
    d[s] = 0
    Q = []
    for v in V:
        heappush(Q, (d[v], v))
    while Q:
        x, u = heappop(Q)
        for v, y in E[u].items():
            alt = d[u] + y
            if d[v] > alt:
                d[v] = alt
                prev[v] = u
                heappush(Q, (alt, v))
    return d, prev

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

# http://sucrose.hatenablog.com/entry/2017/03/20/235434
def extended_euclid(a, b):
    assert a > 0
    assert b > 0
    
    x1, y1, m = 1, 0, a
    x2, y2, n = 0, 1, b
    while m % n != 0:
        q = m / n
        x1, y1, m, x2, y2, n = x2, y2, n, x1 - q * x2, y1 - q * y2, m - q * n
    
    return (x2, y2, n)

class BIT:

    def __init__(self, size):
        self.size = size
        self.xs = [0] * (size + 1)

    def sum(self, n):
        r = 0
        while n:
            r += self.xs[n]
            n &= n - 1
        return r

    def add(self, n, x):
        while n <= self.size:
            self.xs[n] += x
            n += n & -n


def TopologicalSort(nodes, edges, rev_edges):
    '''
    nodes     ... Node[]
    edges     ... Dict[From Node](To Node)
    rev_edges ... Dict[To Node](From Node)
    '''
    rev_edges_num = dict((n, len(rev_edges[n])) for n in nodes)
    L = []
    S = [n for n in nodes if not rev_edges_num[n]]
    while S:
        n = S.pop()
        L.append(n)
        for m in edges[n]:
            rev_edges_num[m] -= 1
            if not rev_edges_num[m]:
                S.append(m)
    
    # プロコン用なのでエラーチェックはしない

    return L
