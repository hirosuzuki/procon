N = int(input())
A = [int(_) for _ in input().split()]

c1 = 0
c2 = 0
c4 = 0
for a in A:
    if a % 2 == 1:
        c1 += 1
    elif a % 4 == 0:
        c4 += 1
    else:
        c2 += 1

if c1 > c4 + 1:
    print("No")
elif c1 == c4 + 1:
    if c2 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")
