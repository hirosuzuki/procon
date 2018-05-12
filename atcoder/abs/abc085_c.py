def solve(N, Y):
    # 10000 * a + 5000 * b + 1000 * c = Y
    # a + b + c = N
    # 0 <= a, b, c

    # 10000 * a + 5000 * b + 1000 * (N - a - b) = Y
    # 9000 * a + 4000 * b = Y - 1000 * N
    # 9 * a + 4 * b = Y / 1000 - N

    # a = ((Y / 1000 - N) - 4 * b) / 9

    t = Y // 1000 - N
    for b in range(9):
        if (t - 4 * b) % 9 == 0:
            a = (t - 4 * b) // 9
            c = N - a - b
            if a < 0 or b < 0 or c < 0:
                return -1, -1, -1
            return a, b, c

N, Y = [int(x) for x in input().split()]

print(*solve(N, Y))
