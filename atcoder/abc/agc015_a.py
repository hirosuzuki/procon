N, A, B = [int(_) for _ in input().split()]

vmin = A * (N - 1) + B
vmax = A + B * (N - 1)

result = vmax - vmin + 1

if result < 0:
    result = 0
    
print(result)
