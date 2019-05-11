N = int(input())
S = [input() for i in range(N)]

def count(s):
    p = 0
    result = 0
    while 1:
        q = s.find("AB", p)
        if q < 0:
            break
        p = q + 2
        result += 1
    return result

result = 0

la = 0
sb = 0
ab = 0

for s in S:
    r = count(s)
    # print("*", s, r)
    if s[-1] == "A":
        la += 1
    if s[0] == "B":
        sb += 1
        if s[-1] == "A":
            ab += 1
    result += r

la -= ab
sb -= ab

#print(la, sb, ab)

f = 0
while 1:
    if f:
        if ab >= 1:
            f = 1
            ab -= 1
            result += 1
        elif sb >= 1:
            f = 0
            sb -= 1
            result += 1
        else:
            break
    else:
        if la >= 1:
            la -= 1
            f = 1
        elif ab >= 1:
            ab -= 1
            f = 1
        else:
            break

#result += min(la, sb, N - 1)

print(result)
