c1 = input()
c2 = input()

if c1[::-1] == c2 and c2[::-1] == c1:
    print("YES")
else:
    print("NO")