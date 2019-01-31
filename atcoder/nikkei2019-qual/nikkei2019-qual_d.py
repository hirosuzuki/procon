N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for i in range(N - 1 + M)]

from collections import defaultdict

nodes = list(range(1, N + 1))
edges = defaultdict(set)
rev_edges = defaultdict(set)

for a, b in AB:
    edges[a].add(b)
    rev_edges[b].add(a)

#print(vs)
#print(ws)

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

L = TopologicalSort(nodes, edges, rev_edges)

nrank = dict((n, r) for r, n in enumerate(L))

for n in range(1, N + 1):
    r = 0
    if rev_edges[n]:
        r = sorted(rev_edges[n], key=lambda x:nrank[x], reverse=True)[0]
    print(r)
