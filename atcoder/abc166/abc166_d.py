X = int(input())

M = 21148

ns = [i**5 for i in range(M)]
n5s = {i**5:i for i in range(M)}

result = None
for i in range(M):
    b = ns[i]
    if b + X in n5s:
        result = n5s[b + X], i
    if X - b in n5s:
        result = i, -n5s[X - b]

print(*result)
