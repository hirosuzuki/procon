N = int(input())
A = [int(_) for _ in input().split()]

xs = sorted(A, reverse=True)

cs = {}

for x in xs:
    cs[x] = cs.get(x, 0) + 1

result = 0

for x in xs:
    if cs[x]:
        for i in range(31, 0, - 1):
            m = 2**i
            y = m - x
            if y > x or y < 1:
                continue
            if y in cs:
                if x == y:
                    if cs[y] >= 2:
                        cs[y] -= 2
                        result += 1
                        break
                else:
                    if cs[y] >= 1:
                        cs[x] -= 1
                        cs[y] -= 1
                        result += 1
                        break

print(cs)
print(result)
