N = int(input())
p = [int(_) - 1 for _ in input().split()]

r = 0

c = 0
for i in range(N):
    if p[i] == i:
        c += 1
    else:
        r += (c + 1) //2 
        c = 0

r += (c + 1) //2 

print(r)
