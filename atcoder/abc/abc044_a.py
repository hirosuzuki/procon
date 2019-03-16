N = int(input())
K = int(input())
X = int(input())
Y = int(input())

result = min(N, K) * X + max(N - K, 0) * Y

print(result)