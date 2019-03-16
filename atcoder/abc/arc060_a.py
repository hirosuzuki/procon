N, A = [int(_) for _ in input().split()]
X = [int(_) for _ in input().split()]

xs = {0: 1}

for n in X:
    #print(xs)
    kv = list(xs.items())
    for k, v in kv:
        nk = k + n - A
        xs[nk] = xs.get(nk, 0) + v

#print(xs)

result = xs[0] - 1

print(result)