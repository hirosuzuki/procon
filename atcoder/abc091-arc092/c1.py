# http://nobuta05.hatenablog.com/entry/2015/11/12/013938

def get_edge(M, u, U=None):

    if U == None:
        for x in M[:]:
            if x[0] == u:
                return x[1]
            elif x[1] == u:
                return x[0]

    else:
        for x in M[:]:
            if x[0] == u and x[1] in U:
                return x[1]
            elif x[1] == u and x[0] in U:
                return x[0]
    return None

def get_nodes(M):
    U = set()
    V = set()
    for x in M:
        U.add(x[0])
        V.add(x[1])
    return (U, V)


def augpath(Si, Ti, M, E):
    (U, V) = get_nodes(M)
    Ti1 = set(x[1] for x in E if x[0] in Si and not x[1] in Ti)
    
    if Ti1 == set():
        return (M, None)

    elif Ti1.difference(V) == set():
        Si1 = set(x[0] for x in M if x[1] in Ti1)
        (M, ui1) = augpath(Si1, Ti.union(Ti1), M, E)

        if ui1 == None:
            return (M, None)

        else:
            v = get_edge(M, ui1)
            if (ui1,v) in M:
                M.remove((ui1,v))

            ui = get_edge(E, v, U=Si)
            if ui:
                M.append((ui,v))
            
            return (M, ui)

    else:
        v = Ti1.difference(V).pop()
        u = get_edge(E, v, U=Si)
        M.append((u,v))

        return (M, u)
    

def Hungary(U0, V0, E):
    U_bef = set()
    M = []
    cnt = 0
    length = len(U0)
    
    # CALC
    while True:

        # INIT
        (U, V) = get_nodes(M)
        u = U0[cnt%length]
        cnt = cnt + 1
        S0 = set()
        S0.add(u)
        T0 = set()

        # 終了条件(すべての頂点から始まる増大道を調べて、マッチング数が変わっていなければ、それ以上増えることはない)
        if cnt % length == 0:
            if U.difference(U_bef) == set():
                break
            U_bef = U.copy()

        # 枝刈り(すでにマッチングしている頂点から始まる道は増大道ではない)
        if u in U:
            continue
        
        #CALC
        (M, u) = augpath(S0, T0, M, E)
    
    return M


N = int(input())
AB = [[int(_) for _ in input().split()] for i in range(N)]
CD = [[int(_) for _ in input().split()] for i in range(N)]

"""
from random import randint
N = 100
AB = [(randint(0, N*2), randint(0, N*2)) for i in range(N)]
CD = [(randint(0, N*2), randint(0, N*2)) for i in range(N)]
print(AB)
print(CD)
"""

E = []

for i in range(N):
    for j in range(N):
        if AB[i][0] < CD[j][0] and AB[i][1] < CD[j][1]:
            E.append((i, j))

M = Hungary(list(range(N)), list(range(N)), E)
print(len(M))
