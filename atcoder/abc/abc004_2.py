c = [input() for i in range(4)]

result = [row[::-1] for row in c[::-1]]

print(*result, sep="\n")
