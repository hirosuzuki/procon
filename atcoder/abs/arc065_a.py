import re

def solve(S):
    r = re.compile(r'^(dreamer|eraser|dream|erase)*$')
    return r.match(S)

S = input()

if solve(S):
    print("YES")
else:
    print("NO")