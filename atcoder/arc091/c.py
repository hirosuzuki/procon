def calc(N, M):
    if N == 1 and M == 1:
        return 1
    if N == 1:
        return M - 2
    if M == 1:
        return N - 2
    # N >= 2 and M >= 2:
    return (N - 2) * (M - 2)

N, M = [int(_) for _ in input().split()]

print(calc(N, M))
