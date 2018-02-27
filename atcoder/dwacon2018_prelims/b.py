s = input()

def cut25(s):
    i = s.find("2")
    if i < 0:
        return "", "", s
    j = s.find("5", i + 1)
    if j < 0:
        return "", "", s
    return "25", s[:i] + s[i+1:j], s[j+1:]

r = 0
while 1:
    x = ""
    y = ""
    while 1:
        a, b, c = cut25(s)
        if a == "":
            break
        y += a
        s = c
        x += b
    if y == "":
        break
    s = x + s
    r += 1

if s != "":
    print(-1)
else:
    print(r)
