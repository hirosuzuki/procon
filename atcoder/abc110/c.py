S = input()
T = input()


chars = "abcdefghijklmnopqrstuvwxyz"

sp = {}
tp = {}

result = True

for i in range(len(S)):
    sc = S[i]
    sx = i
    tc = T[i]
    tx = i
    if not sc in sp:
        sp[sc] = i
    else:
        sx = sp[sc]
    if not tc in tp:
        tp[tc] = i
    else:
        tx = tp[tc]
    if sx != tx:
        result = False
        break

if result:
    print("Yes")
else:
    print("No")
