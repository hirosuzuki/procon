import sys
from random import randint

def solve(caseno):
    A = int(input())
    ty, tx = 2, 2
    cells = [[0] * 100 for i in range(3)]
    counter = 0
    while 1:
        print("%d %d" % (ty, tx), flush=True)
        y, x = [int(_) for _ in input().split()]
        #y = ty + randint(-1, 1)
        #x = tx + randint(-1, 1)
        counter += 1
        #print("# get %d %d (%d %d) %d" % (y, x, ty, tx, counter), file=sys.stderr, flush=True)
        if y == 0 and x == 0:
            return True
        if y == -1 and x == -1:
            return False
        cells[y - 1][x - 1] = 1
        #for row in cells:
        #    print(" ", "".join(str(c) for c in row))
        s = sum(cells[ty-2][tx-2:tx+1]) + sum(cells[ty-1][tx-2:tx+1]) + sum(cells[ty][tx-2:tx+1])
        # print("# sum %d" % (s,), file=sys.stderr, flush=True)
        if s == 9:
            ss = (tx - 2) * 3 + 9
            # print("# tsum %d" % (ss,), file=sys.stderr, flush=True)
            if ss >= A:
                return
            elif ss < A - 6:
                tx += 3
            elif ss < A - 3:
                tx += 2
            else:
                tx += 1

def main():
    T = int(input())
    for i in range(T):
        r = solve(i + 1)
        if r == False:
            break

if __name__ == '__main__':
    main()
