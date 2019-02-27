N = int(input())

for i in range(1, N + 1):
    r = ""
    if i % 2 == 0:
        r += "a"
    if i % 3 == 0:
        r += "b"
    if i % 4 == 0:
        r += "c"
    if i % 5 == 0:
        r += "d"
    if i % 6 == 0:
        r += "e"
    print(r or i)
