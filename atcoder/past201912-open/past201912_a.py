S = input()

def solve(S):
    for c in S:
        if c not in "0123456789":
            return "error"
    return int(S) * 2

print(solve(S))
