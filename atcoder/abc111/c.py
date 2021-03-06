import collections

N = int(input())
V = [int(_) for _ in input().split()]

def calc(vs):
    cs = collections.Counter(vs)
    cs[0] = 0
    return cs.most_common()

ve = calc(V[::2])
vo = calc(V[1::2])

result = 0

if ve[0][0] != vo[0][0]:
    result = N - ve[0][1] - vo[0][1]
else:
    result = N - max(ve[0][1] + vo[1][1], ve[1][1] + vo[0][1])

print(result)

