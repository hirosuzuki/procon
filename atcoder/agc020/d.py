Q = int(input())

def sol(A, B):
    if A == B:
        return "AB" * A
    if A > B:
        m = A / B
        pass
    else:
        if A == 1:
            return "B" * (B // 2) + "A" + "B" * (B - B // 2)
        m1 = B // A
        m2 = B // (A - 1)
        if m1 == m2:


def solve():
    A, B, C, D = [int(x) for x in input().split()]
    print(A, B, C, D)
    s = sol(A, B)
    print(s)
    print(s[C-1:D])

for i in range(Q):
    solve()
