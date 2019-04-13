S = input()

result1 = 0
result2 = 0

for i, c in enumerate(S):
    if i % 2 == 0:
        if c == '0':
            result1 += 1
        else:
            result2 += 1
    else:
        if c == '0':
            result2 += 1
        else:
            result1 += 1

#print(result1, result2)
result = min(result1, result2)
print(result)
