N, M = [int(_) for _ in input().split()]
PY = [[i] + [int(_) for _ in input().split()] + [0] for i in range(M)]

nums = [1] * (N + 1)
PY.sort(key=lambda x:x[2])

for row in PY:
    y = row[1]
    row[3] = nums[y]
    nums[y] += 1

PY.sort(key=lambda x:x[0])

for row in PY:
    print("%06d%06d" % (row[1], row[3]))
