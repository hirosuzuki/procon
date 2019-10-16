N = int(input())

result = [1, 2, 3, 4, 5, 6]

for i in range(N % 30):
    x, y = i % 5, i % 5 + 1
    result[x], result[y] = result[y], result[x]

print(*result, sep="")
