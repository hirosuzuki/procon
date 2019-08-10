N, A, B = [int(_) for _ in input().split()]
SD = [input().split() for i in range(N)]

x = 0

for S, D in SD:
    d = min(B, max(A, int(D)))
    x += (d if S == "East" else -d)

if x < 0:
    print("West", -x)
elif x > 0:
    print("East", x)
else:
    print(0)
