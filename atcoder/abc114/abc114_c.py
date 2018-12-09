N = int(input())

def iter_nums():
    xs = "357"
    while 1:
        for x in xs:
            yield x
        xs = [n + x for n in "357" for x in xs]

result = 0
for s in iter_nums():
    n = int(s)
    if n > N:
        break
    if "3" in s and "5" in s and "7" in s:
        result += 1

print(result)