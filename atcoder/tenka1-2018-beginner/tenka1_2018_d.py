N = int(input())

ss = [[1], [1]]
n = 2

for i in range(1, N):
    l = i + 1
    ss = [ss[i] + [n + i] for i in range(l)]
    ss += [[n + i for i in range(l)]]
    n += l
    if n - 1 >= N:
        break

if n - 1 == N:
    print("Yes")
    print(len(ss))
    for r in ss:
        print(len(r), *r)
else:
    print("No")
