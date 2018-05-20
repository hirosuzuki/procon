import re

def solve0(S):
    r = re.compile(r'^(dreamer|eraser|dream|erase)*$')
    return r.match(S)

def solve(S):
    words = "dreamer", "eraser", "dream", "erase"
    while S:
        for word in words:
            if S.endswith(word):
                S = S[:-len(word)]
                break
        else:
            return False
    return True

S = input()

if solve(S):
    print("YES")
else:
    print("NO")