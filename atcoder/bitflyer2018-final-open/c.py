S = input()

import sys
sys.setrecursionlimit(100000)

N = len(S)
i = 0
result = 0

def calc():
    global i
    global result
    r = 0
    while i < N:
        c = S[i]
        i += 1
        if c == "(":
            if calc():
                r += 1
                result += r
        else: # c == ")":
            return 1
    return 0

while i < N:
    calc()

print(result)

