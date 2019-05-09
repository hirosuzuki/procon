S = input()

def solve(s):
    n = len(s)
    for i in range(n - 2):
        if s[i] == s[i + 1]:
            return i + 1, i + 2
        if s[i] == s[i + 2]:
            return i + 1, i + 3
    if s[n - 2] == s[n - 1]:
        return n - 1, n
    return -1, -1

print(*solve(S))
