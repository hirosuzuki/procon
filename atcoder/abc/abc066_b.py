S = input()

result = 0

for i in range(1, (len(S) - 1) // 2 + 1):
    if S[:i] == S[i:i * 2]:
        result = i * 2

print(result)
