A, B, K = [int(_) for _ in input().split()]

i = 100
c = 0
while 1:
    if A % i == 0 and B % i == 0:
        c += 1
        if c == K:
            result = i
            break
    i -= 1

print(result)
