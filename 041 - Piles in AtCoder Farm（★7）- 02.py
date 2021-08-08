# 041 - Piles in AtCoder Farm（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_ao
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/041-02.cpp

from collections import deque

class Point:
    def __init__(self, px, py):
        self.px = px
        self.py = py

def operator_p(a1, a2):
    return Point(a1.px + a2.px, a1.py + a2.py)

def operator_m(a1, a2):
    return Point(a1.px - a2.px, a1.py - a2.py)

def operator(a1, a2):
    if a1.px < a2.px:
        return True
    if a1.px > a2.px:
        return False
    if a1.py < a2.py:
        return True
    return False

# 点 p1 と p2 の外積を求める
def crs(p1, p2):
    return p1.px * p2.py - p1.py * p2.px

# Step #1. 入力
N = int(input())
_L = [list(map(int,input().split())) for _ in range(N)]
_L.sort()
G = []
for x,y in _L:
    G.append(Point(x, y))

# Step #2. 凸包を求める
G1 = deque()
G2 = deque()
Totsuhou = []
G1.append(G[0])
G2.append(G[0])
G1.append(G[1])
G2.append(G[1])
for i in range(2,N):
    while len(G1) >= 2 and crs(operator_m(G1[len(G1)-1], G1[len(G1)-2]), operator_m(G[i], G1[len(G1)-1])) <= 0:
        G1.pop()
    while len(G2) >= 2 and crs(operator_m(G2[len(G2)-1], G2[len(G2)-2]), operator_m(G[i], G2[len(G2)-1])) >= 0:
        G2.pop()
    G1.append(G[i])
    G2.append(G[i])
G1 = list(G1)
G2 = list(G2)
for i in range(len(G1)):
    Totsuhou.append(G1[i])
for i in range(len(G2)-2,0,-1):
    Totsuhou.append(G2[i])

# Step #3. 各 x に対する下端と上端を求める
ly = [10**10] * 1001
ry = [-10**10] * 1001
for i in range(len(Totsuhou)):
    ax = Totsuhou[(i+0) % len(Totsuhou)].px
    ay = Totsuhou[(i+0) % len(Totsuhou)].py
    bx = Totsuhou[(i+1) % len(Totsuhou)].px
    by = Totsuhou[(i+1) % len(Totsuhou)].py
    if ax > bx:
        ax,bx = bx,ax
        ay,by = by,ay
    if ax == bx:
        ly[ax] = min(ly[ax], ay, by)
        ry[ax] = max(ry[ax], ay, by)
    else:
        for i in range(ax,bx+1):
            v1 = (ay * (bx - i) + by * (i - ax)) // (bx - ax)
            v2 = (ay * (bx - i) + by * (i - ax) + (bx - ax) - 1) // (bx - ax)
            ly[i] = min(ly[i], v2)
            ry[i] = max(ry[i], v1)

# Step #4. 答えを求める
Answer = 0
for i in range(1001):
    if ly[i] <= ry[i]:
        Answer += (ry[i] - ly[i] + 1)
print(Answer - N)