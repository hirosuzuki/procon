S = input()

result = (15 - len(S) + S.count("o")) >= 8

if result:
    print("YES")
else:
    print("NO")
