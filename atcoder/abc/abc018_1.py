ABC = [[i, int(input())] for i in range(3)]

for i, x in enumerate(sorted(ABC, key=lambda e:e[1], reverse=True)):
    x.append(i + 1)

print(*[x[2] for x in ABC], sep="\n")
