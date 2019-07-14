S = input()

result = 0

for x in S.split("+"):
    if "0" not in x:
        result += 1

print(result)
