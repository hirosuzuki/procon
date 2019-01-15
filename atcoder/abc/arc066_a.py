N = int(input())
A = [int(_) for _ in input().split()]

def solve(N, A):
    from collections import Counter
    cs = Counter(A)
    if N % 2 == 1:
        if cs[0] != 1:
            return 0
        if any(cs[i] != 2 for i in range(2, N, 2)):
            return 0
    else:
        if any(cs[i] != 2 for i in range(1, N, 2)):
            return 0
    return (2 ** (N // 2)) % 1000000007

print(solve(N, A))
