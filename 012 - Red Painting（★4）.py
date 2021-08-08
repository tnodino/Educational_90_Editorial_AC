# 012 - Red Painting（★4）
# https://atcoder.jp/contests/typical90/tasks/typical90_l
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/012.cpp

class UnionFind:
    def __init__(self, sz):
        self.par = [-1] * sz

    def root(self, pos):
        if self.par[pos] == -1:
            return pos
        self.par[pos] = self.root(self.par[pos])
        return self.par[pos]

    def unite(self, u, v):
        u = self.root(u)
        v = self.root(v)
        if u == v:
            return
        self.par[u] = v

    def same(self, u, v):
        if self.root(u) == self.root(v):
            return True
        return False

def query1(px, py):
    dx = [-1, 0, 1, 0]
    dy = [ 0, 1, 0,-1]
    for i in range(4):
        sx = px + dx[i]
        sy = py + dy[i]
        if used[sx][sy] == False:
            continue
        hash1 = (px - 1) * W + (py - 1)
        hash2 = (sx - 1) * W + (sy - 1)
        UF.unite(hash1, hash2)
    used[px][py] = True

def query2(px, py, qx, qy):
    if used[px][py] == False or used[qx][qy] == False:
        return False
    hash1 = (px - 1) * W + (py - 1)
    hash2 = (qx - 1) * W + (qy - 1)
    if UF.same(hash1, hash2) == True:
        return True
    return False

# Step #1. 入力
H,W = map(int,input().split())
Q = int(input())

# Step #2. Union Find の初期化
UF = UnionFind(H*W)

# Step #3. クエリ処理
used = [[False] * (W+10) for _ in range(H+10)]
for _ in range(Q):
    ty = list(map(int,input().split()))
    if ty[0] == 1:
        x,y = ty[1],ty[2]
        query1(x, y)
    if ty[0] == 2:
        xa,ya,xb,yb = ty[1],ty[2],ty[3],ty[4]
        Answer = query2(xa, ya, xb, yb)
        if Answer == True:
            print('Yes')
        else:
            print('No')