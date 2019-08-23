N = int(input())

rs = []

i = 1

while N > 0:
    if N & i != 0:
        rs.append(i)
        N -= i
    i *= 2

print(len(rs), *rs, sep="\n")
