H, W = [int(_) for _ in input().split()]
S = [input() for i in range(H)]

def solve(H, W, S):
    s = [row + "." for row in S] + ["." * (W + 1)]
    for y in range(H):
        for x in range(W):
            if s[y][x] == "#" \
                and s[y-1][x] == "." and s[y+1][x] == "." \
                and s[y][x-1] == "." and s[y][x+1] == ".":
                return False
    return True

if solve(H, W, S):
    print("Yes")
else:
    print("No")
