AB = [[int(_) for _ in input().split()] for i in range(3)]

cs = [0] * 4

for a, b in AB:
    cs[a - 1] += 1
    cs[b - 1] += 1

cs.sort()

if cs == [1, 1, 2, 2]:
    print("YES")
else:
    print("NO")