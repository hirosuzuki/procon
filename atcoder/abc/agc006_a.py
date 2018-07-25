N = int(input())
S = input()
T = input()

r = N
while 1:
    s, t = S[N - r:], T[:r]
    # print(s, t)
    if s == t:
        break
    r -= 1

result = N * 2 - r
print(result)
