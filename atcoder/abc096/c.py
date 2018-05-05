H, W = [int(_) for _ in input().split()]
S = [input() for _ in range(H)]

def solve(H, W, S):
    S = [s + "." for s in S] + ["." * (W + 1)]
    for y in range(H):
        for x in range(W):
            if (S[y][x] == "#" and
                S[y][x + 1] == "." and S[y][x - 1] == "." and
                S[y + 1][x] == "." and S[y - 1][x] == "."
            ):
                return False
    return True

if solve(H, W, S):
    print("Yes")
else:
    print("No")
