L, R = [int(_) for _ in input().split()]

def solve(L, R):
    if L // 2019 != R // 2019:
        return 0
    l, r = L % 2019, R % 2019
    if l == 0 or r == 0:
        return 0
    result = min(
        (i * j) % 2019
        for i in range(l, r)
        for j in range(i + 1, r + 1)
    )
    return result

print(solve(L, R))
