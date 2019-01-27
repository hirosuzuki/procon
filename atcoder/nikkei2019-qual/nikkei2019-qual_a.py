N, A, B = [int(_) for _ in input().split()]

print(min(A, B), max(A + B - N, 0))
