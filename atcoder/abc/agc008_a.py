x, y = [int(_) for _ in input().split()]

def solve(x, y):
    d = abs(abs(x) - abs(y))
    if y == 0:
        if x <= 0:
            return d
        return d + 1
    if 0 <= y:
        if 0 <= x <= y:
            return d
        if x < 0:
            return d + 1
        return d + 2
    if y <= 0:
        if x <= y:
            return d
        if 0 <= x:
            return d + 1
        return d + 2

print(solve(x, y))
