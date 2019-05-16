S = input()

def conv(c):
    if c == "O":
        return "A"
    elif c == "A":
        return "O"
    return c

result = "".join(conv(c) for c in S)

print(result)
