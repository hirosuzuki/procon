S = input()

result = 0

n = 0
for i, c in enumerate(S):
    if c == "W":
        result += i - n
        n += 1

print(result)
