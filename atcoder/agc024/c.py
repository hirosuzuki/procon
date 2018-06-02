def solve0(N, A):
    p = -1
    for i, x in enumerate(A):
        if x > p + 1:
            return -1
        p = x
    r = 0
    p = set([0])
    for i in range(N - 1, -1, -1):
        c = 0
        q = set(n - 1 for n in p if n - 1 >= 0)
        q.add(A[i])
        r += len(q)
        if 0 in q:
            r -= 1
        print("*", A[i], c, r, p, q)
        p = q
    return r

def solve(N, A):
    p = -1
    for x in A:
        if x > p + 1:
            return -1
        p = x
    r = 0
    p = [0]
    for i in range(N - 1, -1, -1):
        q = [n - 1 for n in p if n >= 2]
        a = A[i]
        if a > 0 and (not q or q[-1] != a):
            q.append(a)
        r += len(q)
        print("*", A[i], r, p, q)
        p = q
    return r

N = int(input())
A = [int(input()) for _ in range(N)]

print(solve(N, A))
