W, A, B = [int(_) for _ in input().split()]

print(max(abs(A - B) - W, 0))
