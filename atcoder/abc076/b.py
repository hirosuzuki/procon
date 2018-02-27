N = int(input())
K = int(input())

r = 1
for i in range(N):
    r = min(r + K, r * 2)

print(r)
