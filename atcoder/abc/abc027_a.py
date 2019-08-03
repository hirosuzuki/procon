L = [int(_) for _ in input().split()]

L.sort()

if L[0] == L[1]:
    result = L[2]
else:
    result = L[0]

print(result)
