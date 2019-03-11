S = input()

l = 0

for c1, c2 in zip(S, S[1:]):
    if c1 == c2:
        l += 1

result = len(S) - l - 1

print(result)
