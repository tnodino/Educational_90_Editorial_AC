# 009 - Three Point Angle（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_i
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/009.cpp

from math import sqrt, acos, pi
from bisect import bisect_left

class Point:
    def __init__(self, px, py):
        self.px = px
        self.py = py

def operator(a1, a2):
    return Point(a1.px - a2.px, a1.py - a2.py)

def getangle(G):
    # 点 G の偏角を求める
    if G.py >= 0.0:
        I = G.px / sqrt(pow(G.px, 2) + pow(G.py, 2))
        kaku = acos(I) * 180.0 / pi
        return kaku
    else:
        I = G.px / sqrt(pow(G.px, 2) + pow(G.py, 2))
        kaku = acos(I) * 180.0 / pi
        return 360.0 - kaku

def getangle2(I1, I2):
    # [偏角 I1] - [原点] - [偏角 I2] のなす角度を求める
    # 例えば I1 = 240°、I2 = 30°のとき、求める角度は 150°
    res = abs(I1 - I2)
    if res >= 180.0:
        return 360.0 - res
    return res

def solve(pos):
    # 最初に偏角の昇順にソートする
    vec = []
    for i in range(N):
        if i == pos:
            continue
        SA = operator(G[i], G[pos])
        angle = getangle(SA)
        vec.append(angle)
    vec.sort()

    # 点 A を全探索して、最も偏角の大きくなる点 C を二分探索（std::lower_bound）で求める
    ret = 0.0
    for i in range(len(vec)):
        target = vec[i] + 180.0
        pos1 = bisect_left(vec, target)

        # 点 C の候補は高々 2 つに絞れる
        CandIdx1 = pos1 % len(vec)
        CandIdx2 = (pos1 + len(vec) - 1) % len(vec)
        Candidate1 = getangle2(vec[i], vec[CandIdx1])
        Candidate2 = getangle2(vec[i], vec[CandIdx2])
        ret = max(ret, Candidate1, Candidate2)
    return ret

# O(N^3) のアルゴリズム（点 A, B, C を全探索）
def solve_Slow():
    Answer = 0.0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i == j or i == k or j == k:
                    continue
                I1 = getangle(operator(G[i], G[j]))
                I2 = getangle(operator(G[k], G[j]))
                Answer = max(Answer, getangle2(I1, I2))
    return Answer

# O(N^2 log N) のアルゴリズム
def solve_Fast():
    # 点 B を全探索
    Answer = 0.0
    for i in range(N):
        ret = solve(i)
        Answer = max(Answer, ret)
    return Answer

# Step #1. 入力
N = int(input())
G = []
for i in range(N):
    x,y = map(int,input().split())
    G.append(Point(x, y))

# Step #2. 出力
FinalAns = solve_Fast()
print(FinalAns)