N, M = [int(_) for _ in input().split()]
S = [input() for i in range(N)]

def solve(N, M, S):

    def calc(xs):
        t = 0
        for x in xs:
            if x == "#":
                yield 0
                t = 0
            else:
                yield t
                t += 1

    hc = [map(sum, zip(calc(row), list(calc(row[::-1]))[::-1])) for row in S]
    vc = zip(*(map(sum, zip(calc(row), list(calc(row[::-1]))[::-1])) for row in zip(*S)))

    result = sum(
        sum(h * v for h, v in zip(hcr, vcr))
        for hcr, vcr in zip(hc, vc)
    )

    return result

print(solve(N, M, S))