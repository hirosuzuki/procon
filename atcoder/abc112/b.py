N, T = [int(_) for _ in input().split()]
CT = [[int(_) for _ in input().split()] for i in range(N)]

cs = [c for c, t in CT if t <= T]

if cs:
    print(min(cs))
else:
    print("TLE")

