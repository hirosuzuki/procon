N, M, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]

r = 0
if N > M:
    r = 1
elif N < M:
    r = -1
else:
    if A > B:
        r = 1
    elif A < B:
        r = -1
    else:
        r = 0

if r > 0:
    print("Y")
elif r < 0:
    print("X")
else:
    print("Same")