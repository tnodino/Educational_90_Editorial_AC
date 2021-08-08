# 077 - Planes on a 2D Plane（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_by
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/077-03.cpp

from collections import defaultdict

class Edge:
    def __init__(self, t, c, r):
        self.to = t
        self.cap = c
        self.rev = r

class Ford_Fulkerson:
    def __init__(self, sz):
        self.size_ = sz
        self.used = [False] * (self.size_+1)
        self.G = [[] for _ in range(self.size_+1)]

    def add_edge(self, u, v, c):
        self.G[u].append(Edge(v, c, len(self.G[v])))
        self.G[v].append(Edge(u, 0, len(self.G[u]) - 1))

    def dfs(self, pos, to, f):
        if pos == to:
            return f
        self.used[pos] = True
        for i in range(len(self.G[pos])):
            if self.used[self.G[pos][i].to] == True or self.G[pos][i].cap == 0:
                continue
            z = self.dfs(self.G[pos][i].to, to, min(f, self.G[pos][i].cap))
            if z != 0:
                self.G[pos][i].cap -= z
                self.G[self.G[pos][i].to][self.G[pos][i].rev].cap += z
                return z
        return 0

    def max_flow(self, s, t):
        ret = 0
        while True:
            for i in range(self.size_+1):
                self.used[i] = False
            f = self.dfs(s, t, 10**9+7)
            if f == 0:
                break
            ret += f
        return ret

# Step #1. Input
N,T = map(int,input().split())
_L = [list(map(int,input().split())) for _ in range(N)]
AX,AY = [list(i) for i in zip(*_L)]
_L = [list(map(int,input().split())) for _ in range(N)]
BX,BY = [list(i) for i in zip(*_L)]
Map = defaultdict(lambda: -1)
for i in range(N):
    Map[(BX[i], BY[i])] = i

# Step #2. Add Edge
dx = [ 1, 1, 0,-1,-1,-1, 0, 1]
dy = [ 0, 1, 1, 1, 0,-1,-1,-1]
Nex = [[-1] * 8 for _ in range(N)]
Z = Ford_Fulkerson(2*N+10)
for i in range(N):
    for j in range(8):
        tx = AX[i] + dx[j] * T
        ty = AY[i] + dy[j] * T
        Nex[i][j] = Map[(tx, ty)]
        if Nex[i][j] != -1:
            Z.add_edge(i, N + Nex[i][j], 1)
for i in range(N):
    Z.add_edge(2 * N + 1, i, 1)
    Z.add_edge(i + N, 2 * N + 2, 1)

# Step #3. Max Flow
res = Z.max_flow(2 * N + 1, 2 * N + 2)
if res != N:
    print('No')
    exit()

# Step #4. Get Answer
Answer = [0] * N
for i in range(N):
    for j in range(len(Z.G[i])):
        if Z.G[i][j].to > 2 * N or Z.G[i][j].cap == 1:
            continue
        for k in range(8):
            if Nex[i][k] == Z.G[i][j].to - N:
                Answer[i] = k + 1

# Step #5. Output
print('Yes')
print(*Answer)