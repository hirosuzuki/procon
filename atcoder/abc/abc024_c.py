N, D, K = [int(_) for _ in input().split()]
LR = [[int(_) for _ in input().split()] for i in range(D)]
ST = [[int(_) for _ in input().split()] for i in range(K)]

def calc(s, t):
    result = 0
    for i in range(D):
        l, r = LR[i]
        if l <= s <= r:
            if r >= t:
                #print(i, l, r, s)
                result = i + 1
                break
            else:
                #print(i, l, r, s)
                s = r
    return result

def calc_rev(s, t):
    result = 0
    for i in range(D):
        l, r = LR[i]
        if l <= s <= r:
            if l <= t:
                #print(i, l, r, s)
                result = i + 1
                break
            else:
                #print(i, l, r, s)
                s = l
    return result

for s, t in ST:
    #print("*", s, t)
    print(calc(s, t) if t > s else calc_rev(s, t))

