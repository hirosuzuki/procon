def solve(S, DAB):
    return 0

T = int(input())
for i in range(T):
    S = int(input())
    DAB = [[int(_) for _ in input().split()] for j in range(S)]
    print("Case #%d:" % (i + 1), solve(S, DAB))

"""
3
1
1 1 1
5
2 7 12
6 3 11
8 10 1
11 11 12
13 9 14
5
1 3 3
2 2 2
3 1 1
4 2 2
5 3 3
"""