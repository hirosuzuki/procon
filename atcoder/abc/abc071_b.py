from collections import Counter

S = input()

cs = Counter(S)

result = "None"

for i in range(26):
    c = chr(ord("a") + i)
    if c not in cs:
        result = c
        break

print(result)
