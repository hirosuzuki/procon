N = int(input())

b = format(N, 'b')
l = len(b)

f = l % 2

w = 1
x = 1
while True:
    x = x * 2 + f
    if x > N:
        break
    f ^= 1
    w ^= 1

print(("Takahashi", "Aoki")[w])
