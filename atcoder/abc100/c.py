N = int(input())
a = [int(_) for _ in input().split()]

def calc(x):
    r = 0
    while 1:
        x, d = divmod(x, 2)
        if d == 1:
            return r
        r += 1

print(sum(calc(x) for x in a))
