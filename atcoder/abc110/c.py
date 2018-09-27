S = input()
T = input()

def normalize(s):
    pos = {}
    for i, c in enumerate(s):
        if not c in pos:
            pos[c] = i
        yield pos[c]

if all(x == y for x, y in zip(normalize(S), normalize(T))):
    print("Yes")
else:
    print("No")
