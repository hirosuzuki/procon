N = int(input())

def cal(x):
    r = 0
    while x:
        r += x % 10
        x //= 10
    return r

r = 100000
for a in range(1, N):
    b = N - a
    r = min(cal(a) + cal(b), r)

print(r)