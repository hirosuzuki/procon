import collections

N = int(input())
V = [int(_) for _ in input().split()]

def calc(vs):
    r = dict(collections.Counter(vs))
    r[0] = 0
    ri = r.items()
    return sorted(ri, key=lambda x:-x[1])

ve = calc(V[::2])
vo = calc(V[1::2])

result = 0

if ve[0][0] != vo[0][0]:
    result = N - ve[0][1] - vo[0][1]
else:
    result = min(N - ve[0][1] - vo[1][1], N - ve[1][1] - vo[0][1])

print(result)

