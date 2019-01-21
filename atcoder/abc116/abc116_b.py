S = int(input())


x = S
cs = set()
cs.add(x)
i = 1
while 1:
    i += 1
    if x % 2 == 0:
        x //= 2
    else:
        x = x * 3 + 1
    if x in cs:
        break
    cs.add(x)

print(i)
