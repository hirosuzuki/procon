
def solve(N, xy):
    return 0

if __name__ == '__main__':
    #N = int(input())
    #xy = [[int(_) for _ in input().split()] for i in range(N)]
    #print(solve(N, xy))
    pass

import math

def k2(v1, v2):
    return math.atan2(v2[1] - v1[1], v2[0] - v1[0])
    
def k3(v1, v2, v3):
    a = k2(v1, v2)
    b = k2(v1, v3)
    r = a - b
    r %= math.pi
    return r
    
xy = [0, 0], [3, 3], [2, 1]

print(k3(xy[0], xy[1], xy[2]))
print(k3(xy[1], xy[2], xy[0]))
print(k3(xy[2], xy[0], xy[1]))
