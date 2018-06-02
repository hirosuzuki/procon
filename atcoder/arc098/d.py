N = int(input())
A = [int(_) for _ in input().split()]

i = 0
j = 0
x = 0

result = 0

while i < N or j < N:
    while j < N and x & A[j] == 0:
        x |= A[j]
        j += 1
    result += j - i
    x &= ~A[i]
    i += 1
    
print(result)
