N = int(input())
s = input()[:-1].split()

t = {
    "b": "1", "c": "1",
    "d": "2", "w": "2",
    "t": "3", "j": "3",
    "f": "4", "q": "4",
    "l": "5", "v": "5",
    "s": "6", "x": "6",
    "p": "7", "m": "7",
    "h": "8", "k": "8",
    "n": "9", "g": "9",
    "z": "0", "r": "0",
}

result = []

for x in s:
    r = "".join(t.get(c.lower(), "") for c in x)
    if r:
        result.append(r)

print(*result)

