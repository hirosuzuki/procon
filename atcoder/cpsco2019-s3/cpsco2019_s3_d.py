N = int(input())
S = input()

def solve(S):
    c = S[0]
    if c != "R":
        return False
    for t in S[1:-2]:
        if c == "R":
            if t == "B":
                return False
        if c == "G":
            if t == "G":
                return False
        c = t
    if not S[-3:] in ("RGB", "GBB", "BBB"):
        return False
    return True

if solve(S):
    print("Yes")
else:
    print("No")
