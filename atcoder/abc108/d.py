L = int(input())

x = L

xs1 = []
xs2 = []
xs3 = []

for i in range(19):
    c = 18 - i
    xs1.append((i + 1, i + 2, 0))

#print("x=", x)

b = 0

for i in range(20):
    n = 19 - i
    r = 2 ** n
    if x >= r:
        m = n
        x -= r
        b += r
        #print(n, r, x, b)
        break

#print("m=", m)
#print("i=", i)

for i in range(i + 1, 20):
    n = 19 - i
    r = 2 ** n
    if x >= r:
        xs3.append((n + 1, 20, b))
        x -= r
        b += r
        #print(n, r, x, b)

for i in range(m):
    xs2.append((i + 1, i + 2, 2**i))

xs = xs1 + xs2 + xs3

print(20, len(xs))

for x in xs:
    print(*x)
