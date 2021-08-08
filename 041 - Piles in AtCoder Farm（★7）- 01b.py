# 041 - Piles in AtCoder Farm（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_ao
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/041-01b.cpp

from math import gcd

class Point:
    def __init__(self, px, py):
        self.px = px
        self.py = py

def operator_p(a1, a2):
    return Point(a1.px + a2.px, a1.py + a2.py)

def operator_m(a1, a2):
    return Point(a1.px - a2.px, a1.py - a2.py)

# 点 p1 と p2 の外積を求める
def crs(p1, p2):
    return p1.px * p2.py - p1.py * p2.px

# 点 p1, p2, p3 が時計回りか反時計回りか
def ccw(p1, p2, p3):
    va = operator_m(p2, p1)
    vb = operator_m(p3, p2)
    if crs(va, vb) > 0:
        return 1
    if crs(va, vb) < 0:
        return -1
    return 0

# Step #1. 入力
N = int(input())
G = []
for _ in range(N):
    x,y = map(int,input().split())
    G.append(Point(x, y))

# Step #2. コーナーケース
if crs(operator_m(G[1], G[0]), operator_m(G[2], G[0])) == 0:
    cl = min(G[0].px, G[1].px, G[2].px)
    cr = max(G[0].px, G[1].px, G[2].px)
    dl = min(G[0].py, G[1].py, G[2].py)
    dr = max(G[0].py, G[1].py, G[2].py)
    ret = gcd(cr - cl, dr - dl)
    print(ret - 2)
    exit()

# Step #3. 答えの計算
Answer = 0
for i in range(1001):
    for j in range(1001):
        H = Point(i, j)
        cnt = 0
        if ccw(G[0], H, G[1]) == ccw(G[0], H, G[2]):
            cnt += 1
        if ccw(G[1], H, G[2]) == ccw(G[1], H, G[0]):
            cnt += 1
        if ccw(G[2], H, G[0]) == ccw(G[2], H, G[1]):
            cnt += 1
        if cnt == 0:
            Answer += 1

# Step #4. 出力
print(Answer)