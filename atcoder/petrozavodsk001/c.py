
def solve(N):
    print(0, flush=True)
    answer = input()[0]
    if answer == "V":
        return
    st = 0
    stc = answer
    ed = N
    edc = answer
    for i in range(20):
        x = (st + ed) // 2
        print(x, flush=True)
        answer = input()[0]
        if answer == "V":
            return
        if (x - st) % 2 == 0 and stc != answer:
            ed = x
            edc = answer
            continue
        if (x - st) % 2 == 1 and stc == answer:
            ed = x
            edc = answer
            continue
        if (ed - x) % 2 == 0 and edc != answer:
            st = x
            stc = answer
            continue
        if (ed - x) % 2 == 1 and edc == answer:
            st = x
            stc = answer
            continue

    return 0

if __name__ == "__main__":
    N = int(input())
    solve(N)

