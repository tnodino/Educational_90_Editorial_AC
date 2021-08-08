# 049 - Flip Digits 2（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_aw
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/049.cpp

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

# Step #1. 入力
N,M = map(int,input().split())
_L = [list(map(int,input().split())) for _ in range(M)]
C,L,R = [list(i) for i in zip(*_L)]

# Step #2. ソート
tup = []
for i in range(M):
    tup.append((C[i], L[i]-1, R[i]))
tup.sort()

# Step #3. 最小全域木を求める
cnt1 = 0
cnt2 = 0
UF = UnionFind(N+2)
for i in range(len(tup)):
    u = tup[i][1]
    v = tup[i][2]
    if UF.same(u, v) == False:
        UF.unite(u, v)
        cnt1 += tup[i][0]
        cnt2 += 1

# Step #4. 出力
if cnt2 != N:
    print(-1)
else:
    print(cnt1)