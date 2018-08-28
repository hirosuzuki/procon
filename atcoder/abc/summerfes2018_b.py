N = int(input())
S = input()

def solve(N, S):
    result = 0
    for i in range(N + 1):
        if S[:i].count("K") == 0 and S[i:].count("D") == 0:
            result += 1
    return result

print(solve(N, S))