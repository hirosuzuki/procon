A, B = [int(_) for _ in input().split()]

d = B - A

x = 0
for i in range(d):
    x += i

print(x - A)