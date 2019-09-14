N = int(input())
A = [int(input()) for i in range(N)]

cs = sorted(A)

for a in A:
    if cs[-1] == a:
        print(cs[-2])
    else:
        print(cs[-1])

