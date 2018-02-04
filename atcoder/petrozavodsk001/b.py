
def solve(A, B):
    t = 0
    s = 0
    for a, b in zip(A, B):
        if a > b:
            s += a - b
        if b > a:
            x = b - a
            t += x // 2
    if s <= t:
        return True
    else:
        return False

N = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

if solve(A, B):
    print("Yes")
else:
    print("No")
