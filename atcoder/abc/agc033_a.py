H, W = [int(_) for _ in input().split()]
A = [list(input()) for i in range(H)]


ps = []
pcount = 0
for y, row in enumerate(A):
    for x, c in enumerate(row):
        if c == "#":
            ps.append((x, y))
            pcount += 1


result = 0

#print(A)
#print(ps)

while pcount < H * W:
    nps = []
    def pset(x, y):
        global pcount
        if 0 <= y < len(A) and 0 <= x < len(A[y]) and A[y][x] == ".":
            A[y][x] = "#"
            nps.append((x, y))
            pcount += 1
    for x, y in ps:
        pset(x - 1, y)
        pset(x + 1, y)
        pset(x, y - 1)
        pset(x, y + 1)
    ps = nps
    result += 1
    #print(A)
    #print(ps)
    #print(result)

print(result)
