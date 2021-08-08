# 077 - Planes on a 2D Plane（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_by
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/077-02.cpp

from sys import setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**6)

def dfs(pos, pre):
    used[pos] = True
    if pos < N:
        cnt[0] += 1
    if pos >= N:
        cnt[1] += 1
        if AX[pre] < BX[pos - N]:
            Answer[pre] = 1
        if AX[pre] > BX[pos - N]:
            Answer[pre] = 5
    for i in G[pos]:
        if used[i] == True:
            continue
        dfs(i, pos)

# Step #1. Input
N,T = map(int,input().split())
_L = [list(map(int,input().split())) for _ in range(N)]
AX,AY = [list(i) for i in zip(*_L)]
_L = [list(map(int,input().split())) for _ in range(N)]
BX,BY = [list(i) for i in zip(*_L)]
Map = defaultdict(lambda: -1)
for i in range(N):
    Map[BX[i]] = i
    assert(AY[i] == 0)
    assert(BY[i] == 0)

# Step #2. Make Graph
G = [[] for _ in range(N*2)]
for i in range(N):
    idx1 = Map[AX[i] - T]
    idx2 = Map[AX[i] + T]
    if idx1 != -1:
        G[i].append(idx1+N)
        G[idx1+N].append(i)
    if idx2 != -1:
        G[i].append(idx2+N)
        G[idx2+N].append(i)

# Step #3. DFS
cnt = [0] * 2
used = [False] * (N*2)
Answer = [0] * (N*2)
for i in range(N):
    if len(G[i]) >= 2 or used[i] == True:
        continue
    cnt[0] = 0
    cnt[1] = 0
    dfs(i, -1)
    if cnt[0] != cnt[1]:
        print('No')
        exit()

# Step #4. Output
print('Yes')
print(*Answer[:N])