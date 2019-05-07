N = int(input())
CA = []
for i in range(N):
    vs = input().split()
    CA.append((vs[0], int(vs[1])))

m = 1
p = 0
for c, a in CA:
    if c == "*" and a > 0:
        m *= a
    elif c == "+" and a > 0:
        p += a

result = p * m

print(result)
