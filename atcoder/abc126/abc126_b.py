S = input()

def solve(S):
    check1 = 1 <= int(S[0:2]) <= 12
    check2 = 1 <= int(S[2:4]) <= 12
    return {
        (False, False): "NA",
        (False, True):  "YYMM",
        (True,  False): "MMYY",
        (True,  True):  "AMBIGUOUS",
    }[(check1, check2)]

print(solve(S))