N = int(input())
S = [input() for i in range(N)]

CHARS = "abcdefghijklmnopqrstuvwxyz"

result = "".join(c * min(s.count(c) for s in S) for c in CHARS)

print(result)
