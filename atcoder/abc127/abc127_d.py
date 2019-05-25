N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
BC = [tuple(int(_) for _ in input().split()) for i in range(M)]


A = sorted(A)
BC = sorted(BC, key=lambda x:-x[1])

#print(A, BC)

i = 0
for b, c in BC:
    if i > N:
        break
    for j in range(b):
        if i >= N or A[i] >= c:
            break
        A[i] = c
        i += 1
    
#print(A, BC)

result = sum(A)

print(result)
