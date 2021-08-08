# 041 - Piles in AtCoder Farm（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_ao
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/041-01a.cpp

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
V = []
V.append(G[0])
V.append(G[1])
V.append(G[2])

# Step #2. 各 x に対する下端と上端を求める
ly = [10**10] * 1001
ry = [-10**10] * 1001
for i in range(len(V)):
    ax = V[(i+0) % len(V)].px
    ay = V[(i+0) % len(V)].py
    bx = V[(i+1) % len(V)].px
    by = V[(i+1) % len(V)].py
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

# Step #3. 答えを求める
Answer = 0
for i in range(1001):
    if ly[i] <= ry[i]:
        Answer += (ry[i] - ly[i] + 1)
print(Answer - N)