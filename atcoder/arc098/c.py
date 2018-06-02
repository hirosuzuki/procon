N = int(input())
S = input()

l = 0
r = S[1:].count('E')
result = l + r

for i in range(1, N):
    if S[i - 1] == "W":
        l += 1
    if S[i] == "E":
        r -= 1
    result = min(result, l + r)

print(result)
