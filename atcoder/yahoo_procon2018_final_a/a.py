def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def solve(N, M, A):
    for i in range(1, M + 1):
        r = 0
        for n in A:
            if gcd(i, n) == 1:
                r += 1
        print(i, r)

N = 10**5
M = 10**5
A = list(range(1, 10**5+1))
solve(N, M, A)

if __name__ == '__main__':
    N, M = [int(_) for _ in input().split()]
    A = [int(input()) for _ in range(N)]
    solve(N, M, A)
