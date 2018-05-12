def solve(N, A):
    a = sorted(A, reverse=True)
    result = sum(a[::2]) - sum(a[1::2])
    return result

N = int(input())
A = [int(x) for x in input().split()]

print(solve(N, A))
