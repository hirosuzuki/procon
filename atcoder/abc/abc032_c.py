N, K = [int(_) for _ in input().split()]
S = [int(input()) for i in range(N)]

def solve(N, K, S):
    if any(x == 0 for x in S):
        return len(S)
    r = 1
    i = 0
    j = 0
    result = 0
    while i < N:
        while j < N:
            r *= S[j]
            j += 1
            if r > K:
                break
            result = max(result, j - i)
        #print("E", i, j, r)
        if j == N:
            break
        while r > K and i < j:
            r //= S[i]
            i += 1
        #print("S", i, j, r)
    return result


print(solve(N, K, S))
