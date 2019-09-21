N = int(input())
A = [int(_) for _ in input().split()]

# 1 2 3 4 5 6 7 8 9
# s x s x s x s x s
# s x s s x s s x s
# s x s x x x s x s
# 0 1 0 1 2 3 0 1 0

def calc(n):
    tbl = [
        0, 0, 1, 0, 1, 2, 3, 0, 1, 0
    ]
    return tbl[n]

result = sum([calc(a) for a in A])

print(result)
