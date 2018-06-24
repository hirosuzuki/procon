N, M = [int(_) for _ in input().split()]

def calc(N, M):
    MODE = 10**9+7
    if N > M:
        N, M = M, N
    if M > N + 1:
        return 0
    r = 1
    for i in range(1, N + 1):
        r = (r * i) % MODE
    for i in range(1, M + 1):
        r = (r * i) % MODE
    if N == M:
        r = (r * 2) % MODE
    return r

print(calc(N, M))
