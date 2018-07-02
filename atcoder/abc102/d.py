N = int(input())
A = [int(_) for _ in input().split()]

i, j, k = 1, 2, 3
B, C, D, E = A[0], A[1], A[2], sum(A[3:])

result = 10 ** 20

while 1:

    while 1:   
        newB, newC = B + A[i], C - A[i]
        if abs(B - C) < abs(newB - newC):
            break
        i += 1
        B, C = newB, newC

    while 1:   
        newD, newE = D + A[k], E - A[k]
        if abs(D - E) < abs(newD - newE):
            break
        k += 1
        D, E = newD, newE

    r = max(B, C, D, E) - min(B, C, D, E)
    result = min(result, r)

    C, D = C + A[j], D - A[j]
    j += 1
    if j == N - 1:
        break
    
print(result)
