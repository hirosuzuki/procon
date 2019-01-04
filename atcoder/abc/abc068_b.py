N = int(input())

result = 0

for i in range(0, 7):
    if N >= 2**i:
        result = 2**i

print(result)
