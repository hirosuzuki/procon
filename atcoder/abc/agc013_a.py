N = int(input())
A = [int(_) for _ in input().split()]

def solve(N, A):
    s = 0
    result = 1
    for i in range(N-1):
        r = A[i+1] - A[i]
        if r * s < 0:
            result += 1
            s = 0
        elif r != 0:
            s = r
    return result

print(solve(N, A))
