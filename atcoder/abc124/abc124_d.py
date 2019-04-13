N, K = [int(_) for _ in input().split()]

S = input()

xs = []

i = 0

while i < N :
    l = 0
    while i < N and S[i] == '1':
        i += 1
        l += 1
    xs.append(l)
    l = 0
    while i < N and S[i] == '0':
        i += 1
        l += 1
    xs.append(l)

xs += [0] * (K * 2)

#print(xs)

result = 0

l = (K * 2) + 1
result = r = sum(xs[0:l])
#print("*", result, r)

i = 0
while i + l + 1 < len(xs):
    r = r - xs[i] - xs[i+1] + xs[i+l] + xs[i+l+1]
    result = max(result, r)
    #print(result, r)
    i += 2

print(result)
