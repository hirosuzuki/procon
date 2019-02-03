N, M = [int(_) for _ in input().split()]
X = [int(_) for _ in input().split()]
 
xs = sorted(X)
ds = [xs[i + 1] - xs[i] for i in range(M - 1)]
ds = sorted(ds)
 
result = sum(ds[:max(M - N, 0)])
 
print(result)