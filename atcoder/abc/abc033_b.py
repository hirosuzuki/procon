N = int(input())
SP = [input().split() for i in range(N)]

SP = [(s, int(p)) for s, p in SP]

t = sum(p for s, p in SP)
ts = [s for s, p in SP if p > t / 2]

if ts:
    print(ts[0])
else:
    print("atcoder")