N, D = [int(_) for _ in input().split()]
X = [int(_) for _ in input().split()]

#N, D = 5, 7
#X = 11, 13, 17, 19, 23

#N, D = 6, 36
#X = 0, 5, 32, 48, 69, 71

j = 0
r = 0
t = 0
c = []
ct = [0]

for i in range(N):
    x = X[i]
    while X[j] < x - D and j < i:
        j += 1
    c.append(i - j)
    t += i - j
    ct.append(t)

    if i >= 2:
        s = ct[i] - ct[j]
        s -= c[i] * (c[i] - 1) // 2
        r += s

print(r)

