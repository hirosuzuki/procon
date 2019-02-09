K, A, B = [int(_) for _ in input().split()]

def solve(K, A, B):
    r = 1
    if B - A <= 2:
        return r + K
    x = min(A - 1, K)
    r += x
    K -= x
    # print("*", r, K)
    if r >= A:
        x = K // 2
        r += x * (B - A)
        K -= x * 2
    # print("*", r, K)
    r += K
    K -= K
    return r

print(solve(K, A, B))
