S = input()

result = ""
for c in S:
    if c == "0" or c == "1":
        result += c
    elif c == "B" and result != "":
        result = result[:-1]

print(result)