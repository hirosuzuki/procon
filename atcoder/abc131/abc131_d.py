N = int(input())
AB = [tuple([int(_) for _ in input().split()]) for i in range(N)]

AB.sort(key=lambda x:x[1])

result = True

t = 0
for a, b in AB:
    if t + a > b:
        result = False
        break
    else:
        t += a

if result:
    print("Yes")
else:
    print("No")
