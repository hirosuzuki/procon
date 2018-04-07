def TroubleSort(L):
    done = False
    while not done:
        done = True
        for i in range(len(L) - 2):
            if L[i] > L[i+2]:
                done = False
                L[i+2], L[i] = L[i], L[i+2]
    

def solve(caseno, N, V):
    sortedV = sorted(V)
    TroubleSort(V)
    for i in range(len(V)):
        if V[i] != sortedV[i]:
            print("Case #%d:" % caseno, i)
            return
    print("Case #%d:" % caseno, "OK")

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        V = [int(_) for _ in input().split()]
        solve(i + 1, N, V)
