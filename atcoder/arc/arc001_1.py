N = int(input())
C = input()

cs = {i:0 for i in range(1, 5)}

for c in C:
    cs[int(c)] += 1

print(max(cs.values()), min(cs.values()))
