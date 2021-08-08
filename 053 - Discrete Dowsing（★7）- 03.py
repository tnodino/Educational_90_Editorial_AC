# 053 - Discrete Dowsing（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_ba
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/053-03.cpp

def Ask(pos):
    print('?', pos)
    t = int(input())
    return t

def solve():
    N = int(input())
    if N == 1:
        x = Ask(1)
        print('!', x)
    else:
        Answer = 0
        cl = 1
        cr = N
        for i in range(11):
            cm = (cl + cr) // 2
            d0 = Ask(cm + 0)
            d1 = Ask(cm + 1)
            Answer = max(Answer, d0, d1)
            if d0 < d1:
                cl = cm
            else:
                cr = cm
        print('!', Answer)

T = int(input())
for _ in range(T):
    solve()