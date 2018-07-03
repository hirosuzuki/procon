S = input()

CHARS = [chr(ord("a") + i) for i in range(26)]

xs = dict((c, -1) for c in CHARS)
ms = dict((c, -1) for c in CHARS)

for i, c in enumerate(S):
    p = xs[c]
    ms[c] = max(i - p - 1, ms[c])
    xs[c] = i

for c in CHARS:
    ms[c] = max(len(S) - xs[c] - 1, ms[c])

result = min(ms.values())

print(result)