H, W, K = [int(_) for _ in input().split()]
RC = [[int(_) for _ in input().split()] for i in range(K)]

xs = [H] * (W + 1)
ys = [W] * (H + 1)

xs[0] = 0
ys[0] = 0

for y, x in RC:
    xs[x] -= 1
    ys[y] -= 1

from itertools import accumulate

# print("xs", xs)
# print("ys", ys)

def calc(ts):
    ats = list(accumulate(ts))
    # print("a", ats)
    r = sum(d * t for d, t in enumerate(ts))
    result = r
    for i in range(1, len(ts)):
        r = r + (ats[i - 1] - 0) - (ats[-1] - ats[i - 1])
        # print("*", i, r)
        result = min(result, r)
    # print(ts, r)
    return result

result = calc(xs) + calc(ys)

print(result)
