N = int(input())

n = N
m = 0
while n:
    n, d = divmod(n, 10)
    m += d

if N % m == 0:
    print("Yes")
else:
    print("No")

