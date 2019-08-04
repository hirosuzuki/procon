N = int(input())
A = [int(_) for _ in input().split()]

def solve(N, A):
    s = sum(A)
    if s % N != 0:
        return -1
    c = s // N
    result = 0
    for i in range(N - 1):
        if A[i] != c:
            A[i + 1] -= c - A[i]
            A[i] = c
            result += 1
    return result

print(solve(N, A))
