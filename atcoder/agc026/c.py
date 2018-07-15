N = int(input())
S = input()

result = 0

S1 = S[:N]
S2 = S[N:][::-1]

def calc(s, x):
    s1 = ""
    s2 = ""
    for c in s:
        if x & 1:
            s1 += c
        else:
            s2 += c
        x >>= 1
    return s1, s2

from collections import defaultdict

kv = defaultdict(int)

for i in range(2**N):
    kv[calc(S2, i)] += 1

for i in range(2**N):
    result += kv[calc(S1, i)]

print(result)

