S = input()

def is_keyence_str(S):
    for i in range(len(S) + 1):
        for j in range(i, len(S) + 1):
            r = S[:i] + S[j:]
            # print(i, j, r)
            if r == "keyence":
                return True
    return False

if is_keyence_str(S):
    print("YES")
else:
    print("NO")