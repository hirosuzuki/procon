N = int(input())
XY = [tuple([int(_) for _ in input().split()]) for i in range(N)]

if N == 1:

    result = 1

else:

    XY.sort()

    dxy = [
        (XY[i][0] - XY[j][0], XY[i][1] - XY[j][1])
        for i in range(N)
        for j in range(i + 1, N)
    ]

    from collections import Counter

    cdxy = Counter(dxy)

    m = max(cdxy.values())

    #print(XY)
    #print(dxy)
    #print(cdxy)

    result = N - m

print(result)
