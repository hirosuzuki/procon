A = int(input())
B = int(input())

result = min(abs(B - A), abs(B + 10 - A), abs(B - 10 - A))

print(result)