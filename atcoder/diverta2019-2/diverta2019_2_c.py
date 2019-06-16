N = int(input())
A = [int(_) for _ in input().split()]

mxs = sorted(x for x in A if x < 0)
pxs = sorted(x for x in A if x >= 0)

if len(mxs) == 0:
    mxs = [pxs[0]]
    pxs = pxs[1:]

if len(pxs) == 0:
    pxs = [mxs[-1]]
    mxs = mxs[:-1]

#print(mxs, pxs)

result = sum(pxs) - sum(mxs)
print(result)

if len(pxs) == 1:
    for y in mxs:
        print(pxs[0], y)
        pxs[0] -= y
else:
    for y in pxs[:-1]:
        print(mxs[0], y)
        mxs[0] -= y
    print(pxs[-1], mxs[0])
    pxs[-1] -= mxs[0]
    for y in mxs[1:]:
        print(pxs[-1], y)
        pxs[-1] -= y

#for i in range



