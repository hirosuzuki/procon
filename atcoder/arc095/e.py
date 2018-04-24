H, W = [int(_) for _ in input().split()]
S = [input() for i in range(H)]

def check(s):
    xs = sorted(["".join(sorted(x)) for x in S])
    while len(xs) >= 2:
        x = xs.pop(0)
        if x in xs:
            xs.remove(x)
        else:
            return False
    if len(xs) == 1:
        return xs[0] == xs[0][::-1]
    return True

def check1(S):
    if not (check(S) and check(zip(*S))):
        return False
    return True

def ck(s):
    xs = s[:]
    r = []
    while len(xs) >= 2:
        x = xs.pop(0)
        x0 = sorted(x)
        for i, _ in enumerate(xs):
            if sorted(_) == x0:
                del xs[i]
                r = [x] + r + [_]
                break
        else:
            return False
    if len(xs) == 1:
        if xs[0] != xs[0][::-1]:
            return False
        r = r[:len(xs)//2] + [xs[0]] + r[len(xs)//2:]
    return r

def ck2(s):
    xs = list(zip(*s))
    while len(xs) >= 2:
        x = xs.pop(0)
        xr = x[::-1]
        if xr in xs:
            xs.remove(xr)
        else:
            return False
    if len(xs) == 1:
        return xs[0] == xs[0][::-1]
    return True

r = ck(S)
if r == False:
    print("NO")
else:
    if ck2(r):
        print("YES")
    else:    
        print("NO")

#if check(S) and check(zip(*S)):
#    print("YES")
#else:
#    print("NO")
