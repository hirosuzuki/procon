A, B, C, D, E, F = [int(_) for _ in input().split()]

maxr = 0
result = 0, 0

for a in range(31):
    for b in range(31):
        l = 100 * a * A + 100 * b * B
        if l <= F:
            maxs100 = E * l
            d = 0
            while d * D * 100 <= maxs100:
                c1 = (maxs100 - d * D * 100) // (C * 100)
                c2 = (F - l - d * D) // C
                c = min(c1, max(0, c2)) 
                s = c * C + d * D
                w = l + s
                if 0 < w <= F:
                    r = 100 * s / w
                    if r >= maxr:
                        maxr = r
                        result = w, s
                d += 1

print(*result)