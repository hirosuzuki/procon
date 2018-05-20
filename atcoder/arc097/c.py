def solve(s, K):
    cs = sorted(set(s))
    ws = set([])
    for i in range(len(s)):
        c = s[i]
        if c in cs[:2]:
            ws.add(c)
            ws.add(s[i:i+2])
            ws.add(s[i:i+3])
            ws.add(s[i:i+4])
            ws.add(s[i:i+5])
    wss = sorted(ws)
    return wss[K - 1]

s = input()
K = int(input())

print(solve(s, K))
