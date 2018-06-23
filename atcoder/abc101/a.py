S = input()

r = 0
for c in S:
    if c == "+":
        r += 1
    elif c == "-":
        r -= 1

print(r)
