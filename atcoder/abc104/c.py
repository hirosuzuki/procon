D, G = [int(_) for _ in input().split()]
PC = [tuple(int(_) for _ in input().split()) for i in range(D)]

from itertools import product

def calc(D, G, PC, es):
    r = 0
    k = None
    result = 0
    for i, e, pc in zip(range(D), es, PC):
        if e:
            r += (i+1) * 100 * pc[0] + pc[1]
            result += pc[0]
        else:
            k = i
    if r >= G:
        return result, r
    if not k is None:
        d = (k+1)*100
        p = PC[k][0]
        if r + d * (p - 1) >= G:
            n = (G - r + d - 1) // d
            result += n
            r += n * d
            return result, r
    return None, None

result = 10**20

for es in product((0, 1), repeat=D):
    r, score = calc(D, G, PC, es)
    #print(D, G, PC, es, r, score)
    if not r is None:
        result = min(result, r)

print(result)
