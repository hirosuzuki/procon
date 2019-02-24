N = int(input())
XU = [[_ for _ in input().split()] for i in range(N)]

result = 0

for x, u in XU:
    if u == "JPY":
        r = float(x)
    else:
        r = float(x) * 380000.0
    result += r

print(result)
