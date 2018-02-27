
def solve(A, B, C, X):
    r = 0
    for i in range(0, A + 1):
        for j in range(0, B + 1):
            t = i * 500 + j * 100
            if t > X:
                break
            if 0 <= (X - t) / 50 <= C:
                r += 1
    return r

A = int(input())
B = int(input())
C = int(input())
X = int(input())

if __name__ == '__main__':
    print(solve(A, B, C, X))
