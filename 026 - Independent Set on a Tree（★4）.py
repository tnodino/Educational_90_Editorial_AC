# 026 - Independent Set on a Tree（★4）
# https://atcoder.jp/contests/typical90/tasks/typical90_z
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/026.cpp

from sys import setrecursionlimit
setrecursionlimit(10**6)

def dfs(pos, cur):
    col[pos] = cur
    for i in G[pos]:
        if col[i] >= 1:
            continue
        dfs(i, 3-cur)

# Step #1. Input
N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

# Step #2. Graph Coloring
col = [0] * N
dfs(0, 1)

# Step #3. Get Answer
G1,G2 = [], []
for i in range(N):
    if col[i] == 1:
        G1.append(i+1)
    if col[i] == 2:
        G2.append(i+1)
if len(G1) > len(G2):
    print(*G1[:N//2])
else:
    print(*G2[:N//2])