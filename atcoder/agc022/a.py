def solve(S):
    chars = [chr(c) for c in range(ord("a"), ord("z") + 1)]
    cs = dict((c, S.count(c)) for c in chars)
    l = len(S) 
    if l < len(chars):
        return S + sorted(c for c, n in cs.items() if n == 0)[0]
    for i in range(2, l + 1):
        sl = S[:l - i]
        sc = S[l - i]
        sr = S[l - i + 1:]
        msrs = [c for c in sr if c > sc]
        if msrs:
            return sl + sorted(msrs)[0]
    return -1

S = input()
print(solve(S))
