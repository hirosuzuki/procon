H, W = [int(_) for _ in input().split()]
S = [input() for i in range(H)]

cs = [list(row) + ["."] for row in S] + [["."] * (W + 1)]

for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            for dy in range(3):
                for dx in range(3):
                    cs[y + dy - 1][x + dx - 1] = "."

#print(cs)

ns = ["".join(cs[y][:W]) for y in range(H)]

#print(ns)

for y in range(H):
    for x in range(W):
        if ns[y][x] == "#":
            for dy in range(3):
                for dx in range(3):
                    cs[y + dy - 1][x + dx - 1] = "#"

rs = ["".join(cs[y][:W]) for y in range(H)]

#print(rs)

if S == rs:
    print("possible")
    print(*ns, sep="\n")
else:
    print("impossible")