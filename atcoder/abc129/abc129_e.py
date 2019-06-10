L = input()

def calc(L):
    result = 0
    for i in range(0, L + 1):
        for j in range(0, L - i + 1):
            if i + j == i ^ j:
                result += 1
    return result

#for i in range(33):
#    print(i, bin(i), calc(i))

M = 10**9+7

def solve(L):
    if L == 0:
        return 1
    result = 1
    t = 0
    for c in L:
        if c == "1":
            t += 1
            result = (result * 3) % M
        else:
            result = (result * 3 - 2 ** t * 2) % M

    return result

print(solve(L))

