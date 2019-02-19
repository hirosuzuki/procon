N = int(input())
T = [int(_) for _ in input().split()]
M = int(input())
PX = [[int(_) for _ in input().split()] for i in range(M)]

for p, x in PX:
    result = sum(T) - T[p - 1] + x
    print(result)
