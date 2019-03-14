S = {}
S["a"] = list(input())
S["b"] = list(input())
S["c"] = list(input())

k = "a"
while 1:
    if len(S[k]) == 0:
        break
    k = S[k].pop(0)
    # print(S, k)

print(k.upper())
