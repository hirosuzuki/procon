N = int(input())

def iter(cs, n):
    for c in cs:
        if n <= 1:
            yield c
        else:
            for p in iter(cs, n - 1):
                yield c + p
        

for w in iter("abc", N):
    print(w)
