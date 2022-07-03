# 035 - Preserve Connectivity（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_ai
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/035-02.cpp

from sys import setrecursionlimit
setrecursionlimit(10**6)

def build_tree(pos, pre):
    par[0][pos] = pre
    for i in G[pos]:
        if i == pre:
            continue
        depth[i] = depth[pos] + 1
        build_tree(i, pos)

def lca(va, vb):
    if depth[va] < depth[vb]:
        va,vb = vb,va
    for i in range(bits-1,-1,-1):
        if depth[va] - depth[vb] >= (1 << i):
            va = par[i][va]
    if va == vb:
        return va
    for i in range(bits-1,-1,-1):
        if par[i][va] != par[i][vb]:
            va = par[i][va]
            vb = par[i][vb]
    return par[0][va]

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
bits = N.bit_length()
par = [[0] * N for _ in range(bits)]
depth = [0] * N
build_tree(0, 0)
for i in range(1,bits):
    for j in range(N):
        par[i][j] = par[i-1][par[i-1][j]]
Q = int(input())
for _ in range(Q):
    _L = list(map(int,input().split()))
    verts = _L[0]
    if verts == 2:
        va,vb = _L[1],_L[2]
        va -= 1
        vb -= 1
        print(depth[va] + depth[vb] - 2 * depth[lca(va, vb)])