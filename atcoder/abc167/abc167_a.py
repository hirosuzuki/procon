S = input()
T = input()

def check(S, T):
    return T[:-1] == S

if check(S, T):
    print("Yes")
else:
    print("No")