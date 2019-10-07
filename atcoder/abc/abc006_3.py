N, M = [int(_) for _ in input().split()]

def resolve(N, M):
    if M < 2 * N:
        return -1, -1, -1
    if M > 4 * N:
        return -1, -1, -1
    x = M - 2 * N
    c = x // 2
    b = x % 2
    a = N - b - c
    return a, b, c

print(*resolve(N, M))
