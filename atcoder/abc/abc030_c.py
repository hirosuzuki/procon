N, M = [int(_) for _ in input().split()]
X, Y = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]

def solve(N, M, X, Y, A, B):
    result = 0
    t = 0
    ai = bi = 0
    while True:
        while ai < len(A) and A[ai] < t:
            ai += 1
        if ai >= len(A):
            break
        #print("A", ai, A[ai], t)
        t = A[ai] + X
        while bi < len(B) and B[bi] < t:
            bi += 1
        if bi >= len(B):
            break
        #print("B", bi, B[bi], t)
        t = B[bi] + Y
        result += 1
        #print("r", result, t)
    return result

result = solve(N, M, X, Y, A, B)

print(result)

