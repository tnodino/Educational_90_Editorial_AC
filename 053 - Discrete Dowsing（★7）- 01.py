# 053 - Discrete Dowsing（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_ba
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/053-01.cpp

def Ask(pos):
    print('?', pos)
    t = int(input())
    return t

def solve():
    N = int(input())
    Answer = 0
    for i in range(1,N+1):
        Answer = max(Answer, Ask(i))
    print('!', Answer)

T = int(input())
for _ in range(T):
    solve()