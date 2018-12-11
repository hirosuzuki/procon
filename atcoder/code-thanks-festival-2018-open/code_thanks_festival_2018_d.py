S = input()

lc = "z"
result = 0
for c in S:
    if c <= lc:
        result += 1
        lc = c

print(result)