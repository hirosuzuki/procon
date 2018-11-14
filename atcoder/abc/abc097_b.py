X = int(input())

result = 1

for i in range(2, 33):
    for j in range(2, 11):
        r = i**j
        if r <= X:
            result = max(result, r)

print(result)
