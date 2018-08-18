S = input()
K = int(input())

c = ""
for r in range(len(S)):
    c = S[r]
    if c != "1":
        break

if K <= r:
    result = "1"
else:
    result = c

print(result)
