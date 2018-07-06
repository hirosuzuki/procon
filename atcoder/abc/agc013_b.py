from collections import defaultdict
N, M = [int(_) for _ in input().split()]
V = defaultdict(list)
for i in range(M):
    A, B = [int(_) for _ in input().split()]
    V[A].append(B)
    V[B].append(A)

def solve(N, M, V):
    result = [1, V[1][0]]
    used = [False] * (N + 1)
    for x in result:
        used[x] = True

    def check_edge(i):
        for e in V[result[i]]:
            if not used[e]:
                if i == -1:
                    result.append(e)
                else:
                    result.insert(i, e)
                used[e] = True
                return True
        return False

    while True:
        if check_edge(0): continue
        if check_edge(-1): continue
        return result

result = solve(N, M, V)
print(len(result))
print(*result)
