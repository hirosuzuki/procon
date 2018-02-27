S = input()
T = input()

from fnmatch import fnmatch

for i in range(len(S) - len(T), -1, -1):
    if fnmatch(T, S[i:i + len(T)]):
        r = S[:i] + T + S[i + len(T):]
        r = r.replace("?", "a")
        print(r)
        break
else:
    print("UNRESTORABLE")
