S = input()

def solve(S):
    if S[0] != "A":
        return False
    s = S[1:]        
    if not "C" in s[1:-1]:
        return False
    i = s[1:-1].find("C") + 1
    s = s[:i] + s[i+1:]
    for c in s:
        if c < "a" or c > "z":
            return False
    return True

if solve(S):
    print("AC")
else:
    print("WA")
