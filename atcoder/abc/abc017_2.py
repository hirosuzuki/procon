X = input()

def check(s):
    if s == "":
        return True
    if s[0] in "oku":
        return check(s[1:])
    if s[:2] == "ch":
        return check(s[2:])
    return False

if check(X):
    print("YES")
else:
    print("NO")