N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

w = sum(x for x in A[K:] if x > 0)
b = sum(A[:K]) + w

result = max(w, b)

for i in range(N - K):
    j = i + K
    Ai = A[i]
    Aj = A[j]
    if Ai > 0:
        w += Ai
    if Ai < 0:
        b -= Ai
    if Aj > 0:
        w -= Aj
    if Aj < 0:
        b += Aj
    result = max(result, w, b)

print(result)
