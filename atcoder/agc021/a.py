def calc(x):
    r = 0
    while x:
        r += x % 10
        x = x // 10
    return r

def solve0(N):
    r = max(calc(i) for i in range(N + 1))
    return r

def solve(N):
    if N < 10:
        return N
    x = N % 10
    if x == 9:
        return solve(N // 10) + x
    else:
        return solve(N // 10 - 1) + 9

N = int(input())

print(solve(N))


