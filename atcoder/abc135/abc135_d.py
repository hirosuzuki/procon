S = input()

rs = [0] * 13

M = 10**9 + 7

if S[-1] == "?":
    rs[:10] = [1] * 10
else:
    rs[int(S[-1])] = 1

for i in range(1, len(S)):
    nrs = [0] * 13
    c = S[-i - 1]
    if c == "?":
        ns = range(10)
    else:
        ns = [int(c)]
    for n in ns:
        r = (10 ** (i % 6)) * n % 13
        for j in range(13):
            jj = (j + r) % 13
            nrs[jj] = (nrs[jj] + rs[j]) % M
    rs = nrs

# print(rs)
print(rs[5])

