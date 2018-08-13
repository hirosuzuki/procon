H, W = [int(_) for _ in input().split()]

def solve(H, W):
    if H % 3 == 0:
        return 0
    result = H * W
    H1 = H // 2
    H2 = H - H1
    for x in range(W + 1):
        a = H * x
        b = (W - x) * H1
        c = (W - x) * H2
        r = max(a, c) - min(a, b)
        result = min(result, r)
        W1 = (W - x) // 2
        W2 = W - x - W1
        b = H * W1
        c = H * W2
        r = max(a, c) - min(a, b)
        result = min(result, r)
    return result

# print(H, W)

result = min(solve(H, W), solve(W, H))

print(result)