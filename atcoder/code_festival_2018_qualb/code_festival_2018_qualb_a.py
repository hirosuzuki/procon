N = int(input())

result = 100

for i in range(1, 101):
    if i % N == 0:
        result -= 1

print(result)
