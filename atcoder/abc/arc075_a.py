N = int(input())
S = [int(input()) for i in range(N)]

t = sum(S)
xs = sorted(x for x in S if x % 10)

if t % 10:
    print(t)
else:
    if xs:
        print(t - xs[0])
    else:
        print(0)
