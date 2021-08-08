# 053 - Discrete Dowsing（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_ba
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/053-02.cpp

def Ask(pos):
    print('?', pos)
    t = int(input())
    return t

def solve():
    N = int(input())
    Answer = 0
    cl = 1
    cr = N + 1
    for i in range(20):
        c1 = (cl + cl + cr) // 3
        c2 = (cl + cr + cr) // 3
        d1 = Ask(c1)
        d2 = Ask(c2)
        Answer = max(Answer, d1, d2)
        if d1 < d2:
            cl = c1
        else:
            cr = c2
    print('!', Answer)

T = int(input())
for _ in range(T):
    solve()