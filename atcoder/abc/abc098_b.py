N = int(input())
S = input()

result = max(sum(c in S[i:] for c in set(S[:i])) for i in range(N))

print(result)
