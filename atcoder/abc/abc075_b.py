H, W = [int(_) for _ in input().split()]

S = ["."*(H+2)] + ["." + input() + "." for i in range(H)] + ["."*(H+2)]

for y in range(H):
    for x in range(W):
        c = S[y+1][x+1]
        if c != "#":
            c = str(sum([S[i][x:x+3].count("#") for i in range(y,y+3)]))
        print(c, sep="", end="")
    print()