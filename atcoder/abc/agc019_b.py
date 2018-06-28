A = input()
#A = "abracadabra"

result = 1

for i in range(len(A)):
    m = A[:i+1]
    k = 0
    for i in range(len(m)):
        s = m[i:]
        if s != s[::-1]:
            k += 1
    print(m, k)
    result += k

print(result)

s1 = [A]
for i in range(1, len(A) + 1):
    for j in range(i):
        r = A[j:i]
        rr = r[::-1]
        if r != rr:
            s = A[:j] + rr + A[i:]
            s1.append(s)
print(*sorted(s1), sep="\n")
