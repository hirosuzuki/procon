N = int(input())
xs = [input() for i in range(N)]

result = 0

oldrow = "." * 9

for row in xs:
    for c, oldc in zip(row, oldrow):
        if c == "x" or (c == "o" and oldc != "o"):
            result += 1
    oldrow = row

print(result)
