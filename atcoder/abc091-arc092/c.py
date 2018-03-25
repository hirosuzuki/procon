N = int(input())
AB = [tuple(int(_) for _ in input().split()) for i in range(N)]
CD = [tuple(int(_) for _ in input().split()) for i in range(N)]

AB.sort(key=lambda xy:xy[1], reverse=True)
CD.sort()
for c, d in CD:
    for a, b in AB:
        if a < c and b < d:
            AB.remove((a, b))
            break

print(N - len(AB))
