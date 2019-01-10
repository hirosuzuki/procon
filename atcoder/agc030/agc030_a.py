A, B, C = [int(_) for _ in input().split()]

result = 0

if C >= 1:
    C -= 1
    result += 1
    
if B < C:
    result += B + B
    C -= B
    result += min(A, C)
else:
    result += B + C

print(result)