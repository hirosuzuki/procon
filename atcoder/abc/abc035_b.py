S = input()
T = int(input())

x, y, n  = 0, 0, 0
for c in S:
    if c == "L":
        x -= 1
    elif c == "R":
        x += 1
    elif c == "U":
        y += 1
    elif c == "D":
        y -= 1
    else:
        n += 1

if x < 0:
    x = -x
if y < 0:
    y = -y

if T == 2:
    r = min(x, n)
    n -= r
    x -= r
    r = min(y, n)
    n -= r
    y -= r
    n = n % 2

result = x + y + n

print(result)
