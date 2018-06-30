S = input()
Q = int(input())
A = [int(_) for _ in input().split()]
BX = [[int(_) for _ in input().split()] for i in range(Q)]

MOD = 1000000007

i = 0
s = ""
for c in S:
    if c == "a":
        s += "a[%d]" % i
        i += 1
    else:
        s += c

for b, x in BX:
    a = A[:]
    a[b - 1] = x
    print(eval(s) % 1000000007)
