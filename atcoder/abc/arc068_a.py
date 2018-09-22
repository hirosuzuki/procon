X = int(input())

n, m = divmod(X, 11)

r = n * 2

if m == 0:
    pass
elif 1 <= m <= 6:
    r += 1
else:
    r += 2

print(r)