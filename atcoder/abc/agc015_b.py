S = input()

result = 0

N = len(S)

for i, c in enumerate(S):
    if c == "U":
        result += (N - i - 1) + i * 2
    else: # c == "D"
        result += (N - i - 1) * 2 + i

print(result)

