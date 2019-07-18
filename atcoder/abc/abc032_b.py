S = input()
K = int(input())

def solve(S, K):
    if len(S) < K:
        return 0
    s = set()
    for i in range(len(S) - K + 1):
        s.add(S[i:i+K])
    return len(s)

print(solve(S, K))