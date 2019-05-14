N = int(input())
AB = [tuple([int(_) for _ in input().split()]) for i in range(N)]
CD = [tuple([int(_) for _ in input().split()]) for i in range(N)]

AB = sorted(AB, key=lambda x:x[1])
CD = sorted(CD, key=lambda x:x[0])

result = 0

for c, d in CD:
    xs = [x for x in AB if x[0] < c and x[1] < d]
    if xs:
        AB.remove(xs[-1])
        result += 1

print(result)


