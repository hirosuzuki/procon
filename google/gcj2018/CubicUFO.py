from math import *

def calc1(x, y, cosX):
    #print("c", cosX)
    sinX = sqrt(1.0 - cosX**2)
    #print("s", sinX)
    return x * cosX + y * sinX, - x * sinX + y * cosX

def solve(caseno, A):
    cosX = A / sqrt(2)
    #r = pi / 4 - acos(cosX)
    #print(r)
    R = sqrt(2)/4
    x1, y1 = calc1(R, R, cosX)
    x2, y2 = calc1(-R, R, cosX)
    print("Case #%d:" % caseno)
    print(x1, y1, 0)
    print(x2, y2, 0)
    print(0, 0, 0.5)

if __name__ == "__main__":
    T = int(input())
    for caseno in range(1, T + 1):
        solve(caseno, float(input()))
