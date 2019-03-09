A, B = [int(_) for _ in input().split()]

"""
r = 0
for i in range(17):
    r ^= i
    print(i, ("0000" + bin(r)[2:])[-5:])
"""

def calc(n):
    rs = []
    rs.append((n + 1) // 2 % 2)
    for i in range(1, 41):
        d = 1 << i
        x = n // d
        if x % 2 == 0:
            r = 0
        else:
            r = n % 2 ^ 1
        rs.append(r)
    return rs

b1 = calc(A - 1)
b2 = calc(B)

#print(b1)
#print(b2)

result = 0
for i in range(41):
    result |= (b1[i] ^ b2[i]) << i

print(result)
