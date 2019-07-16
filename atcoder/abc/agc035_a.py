N = int(input())
A = [int(_) for _ in input().split()]

from collections import Counter

def solve(N, A):
    cs = Counter(A)
    k = list(cs.keys())
    v = list(cs.values())
    # print(k, v)
    if len(k) == 1 and A[0] == 0:
        return True
    if len(k) == 3 and k[0] ^ k[1] ^ k[2] == 0 and v[0] == v[1] == v[2]:
        return True
    if len(k) == 2 and k[0] == 0 and v[0] * 2 == v[1]:
        return True
    if len(k) == 2 and k[1] == 0 and v[1] * 2 == v[0]:
        return True
    return False

if solve(N, A):
    print("Yes")
else:
    print("No")
