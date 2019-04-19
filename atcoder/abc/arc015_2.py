N = int(input())
T = [[float(_) for _ in input().split()] for i in range(N)]

results = [0] * 6

for MT, mT in T:
    if 35.0 <= MT:
        results[0] += 1
    if 30.0 <= MT < 35.0:
        results[1] += 1
    if 25.0 <= MT < 30.0:
        results[2] += 1
    if 25.0 <= mT:
        results[3] += 1
    if mT < 0 and MT >= 0:
        results[4] += 1
    if MT < 0:
        results[5] += 1

print(*results)
