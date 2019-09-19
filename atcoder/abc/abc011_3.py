N = int(input())
NG = [int(input()) for i in range(3)]

x = N
for j in range(100):
    if x in NG:
        break
    for i in range(3, 0, -1):
        if x - i not in NG:
            x -= i
            break
    else:
        break
    if x <= 0:
        break

if x <= 0:
    print("YES")
else:
    print("NO")