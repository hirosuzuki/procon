X = input()

result = 0

scount = 0

for c in X:
    if c == "T":
        if scount >= 1:
            scount -= 1
        else:
            result += 1
    else:
        scount += 1

print(result * 2)
