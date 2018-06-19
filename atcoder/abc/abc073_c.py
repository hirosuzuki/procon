N = int(input())
A = [int(input()) for i in range(N)]

xs = {}
r = 0

for a in A:
    if a in xs and xs[a] == 1:
        xs[a] = 0
        r -= 1
    else:
        xs[a] = 1
        r += 1

print(r)
