N = int(input())
P = [int(input()) for i in range(N)]

def calc(n):
    r = 0
    while 1:
        n, d = divmod(n, 10)
        if d > 0:
            return r
        r += 1

print(min(calc(x) for x in P))
