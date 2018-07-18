N = int(input())
A = [int(_) for _ in input().split()]

t = sum(A)

if t % 2 == 0:
    print("YES")
else:
    print("NO")
