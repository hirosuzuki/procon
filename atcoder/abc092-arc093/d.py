A, B = [int(_) for _ in input().split()]

patA, patB = "#."

if A > B:
    A, B = B, A
    patA, patB = patB, patA

h, w = 80, 100

rows = [[patB] * w for _ in range(h)]

for i in range(B):
    x = i % (w // 4) * 4
    y = i // (w // 4) * 4
    rows[y][x:x+3] = patA, patA, patA
    rows[y+1][x:x+3] = patA, patA, patA
    rows[y+2][x:x+3] = patA, patA, patA
    if i < A - 1:
        rows[y+1][x+1] = patB

print(h, w)
for row in rows:
    print("".join(row))
