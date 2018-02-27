def solve(r, c, rows):
    areas = []
    def fillarea(x, y):
        area = []
        stack = []
        stack.append((x, y))
        while stack:
            x, y = stack.pop()
            if rows[y][x] == False: continue
            area.append((x, y))
            rows[y][x] = False
            if 0 < x and rows[y][x - 1] == True:
                stack.append((x - 1, y))
            if 0 < y and rows[y - 1][x] == True:
                stack.append((x, y - 1))
            if x < c - 1 and rows[y][x + 1] == True:
                stack.append((x + 1, y))
            if y < r - 1 and rows[y + 1][x] == True:
                stack.append((x, y + 1))
        areas.append(area)
    for y in range(r):
        for x in range(c):
            if rows[y][x]:
                fillarea(x, y)
    def calc(area):
        c1 = sum((x + y) % 2 == 0 for x, y in area)
        c2 = sum((x + y) % 2 == 1 for x, y in area)
        r = max(c1, c2)
        return r
    print("areas", len(areas))
    rsum = sum(calc(area) for area in areas)
    return rsum

#r, c = [int(x) for x in input().split()]
#rows = [[c=="." for c in input()] for i in range(r)]

r, c = 10, 10
import random
rows = [[random.choice([False, False, True, True]) for j in range(c)] for i in range(r)]
print(rows)

for row in rows:
    print("".join("*."[e] for e in row))

print(solve(r, c, rows))
