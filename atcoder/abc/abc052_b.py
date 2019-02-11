N = int(input())
S = input()

result = r = 0

for c in S:
    r += (c == "I") - (c == "D")
    result = max(result, r)

print(result)