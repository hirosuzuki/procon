N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]

def solve(N, A, B):
    xs = [a - b for a, b in zip(A, B)]
    if sum(xs) < 0:
        return -1
    xs.sort()
    rxs = xs[:]
    # print(xs)
    i = 0
    j = len(xs) - 1
    while xs[i] < 0:
        l = -xs[i]
        while l > 0:
            d = min(l, xs[j])
            l -= d
            xs[j] -= d
            if xs[j] == 0:
                j -= 1
        xs[i] = 0
        i += 1
    # print(xs)
    return sum(a != b for a, b in zip(rxs, xs))

print(solve(N, A, B))
