S = input()

cs = [[S[0], 1]]

for c in S[1:]:
    if c == cs[-1][0]:
        cs[-1][1] += 1
    else:
        cs.append([c, 1])

result = "".join(c + str(n) for c, n in cs)

print(result)