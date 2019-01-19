O = input()
E = input()

result = ""

while O + E:
    c1, O = O[:1], O[1:]
    c2, E = E[:1], E[1:]
    result += c1 + c2

print(result)
