# 059 - Many Graph Queries（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_bg
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/059-01.cpp

N,M,Q = map(int,input().split())
_L = [list(map(int,input().split())) for _ in range(M)]
X,Y = [list(i) for i in zip(*_L)]
for i in range(M):
    X[i] -= 1
    Y[i] -= 1
g = [0] * M
for i in range(M):
    g[i] = Y[i] * N + X[i]
g.sort()
for i in range(M):
    X[i] = g[i] % N
    Y[i] = g[i] // N
for _ in range(Q):
    A,B = map(int,input().split())
    A -= 1
    B -= 1
    vis = [False] * N
    vis[A] = True
    for i in range(M):
        if vis[X[i]]:
            vis[Y[i]] = True
    print('Yes' if vis[B] else 'No')