N = int(input())
S1 = input()
S2 = input()

M = 1000000007

c = 0
i = 0
result = 1

while i < N:
    if S1[i] == S2[i]:
        if c == 0:
            result = (result * 3) % M
        elif c == 1:
            result = (result * 2) % M
        elif c == 2:
            result = (result * 1) % M
        c = 1
        i += 1
    else:
        if c == 0:
            result = (result * 3 * 2) % M
        elif c == 1:
            result = (result * 2) % M
        elif c == 2:
            result = (result * 3) % M
        c = 2
        i += 2

print(result)
