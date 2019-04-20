N = int(input())
S = input()


r = S.count(".")
result = r
for i in range(N):
    if S[i] == "#":
        r += 1
    else:
        r -= 1
    result = min(result, r)

print(result)
