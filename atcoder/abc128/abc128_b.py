N = int(input())
SP = [input().split() for i in range(N)]

rs = [(i + 1, sp[0], int(sp[1])) for i, sp in enumerate(SP)]

for r in sorted(rs, key=lambda x:(x[1], -x[2])):
    print(r[0])