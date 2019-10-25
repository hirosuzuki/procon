S = input()
T = input()

def solve(S, T):
    for s, t in zip(S, T):
        if (s == t) or (s == "@" and t in "atcoder") or (t == "@" and s in "atcoder"):
            pass
        else:
            return False
    return True

if solve(S, T):
    print("You can win")
else:
    print("You will lose")
