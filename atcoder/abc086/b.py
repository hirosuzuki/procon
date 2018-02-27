def solve(a, b):
    r = int(a + b)
    t = 1
    while r > 0:
        r -= t
        t += 2
    return r == 0

a, b = input().split()

if solve(a, b):
    print("Yes")
else:
    print("No")
