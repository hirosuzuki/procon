def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

N = int(input())

if N == 3:
    print("2 5 63")
    import sys
    sys.exit()

A = []
for i in range(3, 30001):
    if len(A) == N - 1:
        break
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        A.append(i)

s = sum(A)
if s % 2 == 1:
    A[0] = 2
s = sum(A)
    
l = 30000 - s % 30
A.append(l)
print(" ".join(str(n) for n in A))

