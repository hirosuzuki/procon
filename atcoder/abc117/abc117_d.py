N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

MB = 50

bits = [0] * (MB + 1)

for i in range(MB):
    for a in A:
        if a & (1 << i):
            bits[i] += 1

#print(bits)

def calc(k):
    r = 0
    for j in range(0, MB):
        if k & (1 << j):
            r += max(bits[j], N - bits[j]) << j
        else:
            r += bits[j] << j
    return r

result = calc(K)

for i in range(0, MB):
    m = 1 << i
    if K & m:
        k = K ^ m | (m - 1)
        r = calc(k)
        # print(k, r)
        result = max(result, r)

print(result)

