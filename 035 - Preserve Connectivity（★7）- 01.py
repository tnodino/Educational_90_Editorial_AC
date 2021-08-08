# 035 - Preserve Connectivity（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_ai
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/035-01.cpp

def tree_dp(pos, pre):
    for i in G[pos]:
        if i == pre:
            continue
        tree_dp(i, pos)
        c[pos] += c[i]

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
Q = int(input())
for _ in range(Q):
    _L = list(map(int,input().split()))
    verts = _L[0]
    sel = _L[1:]
    for i in range(verts):
        sel[i] -= 1
    c = [0] * N
    for i in range(verts):
        c[sel[i]] += 1
    tree_dp(sel[0], -1)
    need = 0
    for i in range(N):
        if i != sel[0] and c[i] != 0:
            need += 1
    print(need)
