# 053 - Discrete Dowsing（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_ba
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/053-04.cpp

idx = [0] * 1610
fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

def Ask(pos):
    if idx[pos] == -1:
        print('?', pos)
        t = int(input())
        idx[pos] = t
        return t
    return idx[pos]

def solve():
    N = int(input())
    Answer = 0
    for i in range(N+1):
        idx[i] = -1
    for i in range(N+1,1601):
        idx[i] = -i
    if N <= 5:
        for i in range(1,N+1):
            Answer = max(Answer, Ask(i))
    else:
        cl = 0
        cr = 1597
        dl = 610
        dr = 987
        el = Ask(dl)
        er = Ask(dr)
        Answer = max(Answer, el, er)
        if el < er:
            cl = dl
            dl = dr
            dr = -1
            el = er
            er = -1
        else:
            cr = dr
            dr = dl
            dl = -1
            er = el
            el = -1
        for i in range(12,-1,-1):
            if dl == -1:
                dl = cl + fib[i]
                el = Ask(dl)
            elif dr == -1:
                dr = cr - fib[i]
                er = Ask(dr)
            Answer = max(Answer, el, er)
            if el < er:
                cl = dl
                dl = dr
                dr = -1
                el = er
                er = -1
            else:
                cr = dr
                dr = dl
                dl = -1
                er = el
                el = -1
        for i in range(cl+1,cr):
            Answer = max(Answer, Ask(i))
    print('!', Answer)

T = int(input())
for _ in range(T):
    solve()