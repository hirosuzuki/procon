N = int(input())
A = input()
B = input()
C = input()

result = 0

for a, b, c in zip(A, B, C):
    if a == b == c:
        pass
    elif a == b or b == c or a == c:
        result += 1
    else:
        result += 2

print(result)
