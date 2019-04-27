N = int(input())
A = [int(_) for _ in input().split()]

from fractions import gcd

xs1 = []

r = A[0]
for x in A:
    r = gcd(x, r)
    xs1.append(r)

xs2 = []

r = A[-1]
for x in A[::-1]:
    r = gcd(x, r)
    xs2.append(r)

xs2 = xs2[::-1]

#print(xs1)
#print(xs2)

result = max(xs1[-2], xs2[1])

for i in range(N - 2):
    r = gcd(xs1[i], xs2[i + 2])
    result = max(result, r)

print(result)
