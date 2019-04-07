T = int(input())

def solve(N, P):
    result = "".join({"E":"S", "S":"E"}[x] for x in P)
    return result

for i in range(T):
    N = int(input())
    P = input()
    print("Case #%d:" % (i + 1), solve(N, P))
