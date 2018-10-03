H, W = [int(_) for _ in input().split()]

C = [input() for i in range(H)]

C = ["x" + c + "x" for c in C]

C[0] = C[0].replace(".", "s")

for i in range(1, H - 1):
    S = C[i - 1]
    T = list(C[i])
    for x in range(1, W + 1):
        if T[x] == "." and ("s" in S[x-1:x+2]):
            T[x] = "s"
    C[i] = "".join(T)

result = ""
x = C[H - 1].find("s")

for i in range(H - 1):
    T = C[H - 2 - i]
    if T[x] == "s":
        result += "S"
    elif T[x - 1] == "s":
        result += "L"
        x -= 1
    elif T[x + 1] == "s":
        result += "R"
        x += 1
    else:
        break

if len(result) == H - 1:
    print(result)
else:
    print("impossible")