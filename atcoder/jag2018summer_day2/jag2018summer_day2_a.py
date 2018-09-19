X, Y, Z = [int(_) for _ in input().split()]

r = Z
while 1:
    if r % 17 == X and r % 107 == Y:
        break
    r += 1000000007

print(r)
