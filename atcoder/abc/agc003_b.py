N = int(input()) 
A = [int(input()) for i in range(N)]

result = 0

t = 0
for a in A:
    if a == 0:
        result += t // 2
        t = 0
    else:
        t += a

result += t // 2

print(result)