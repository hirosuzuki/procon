S = input()

r = S.count("0")
b = len(S) - r

result = len(S) - abs(r - b)

print(result)