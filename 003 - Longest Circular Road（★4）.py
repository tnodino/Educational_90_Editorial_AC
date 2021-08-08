# 003 - Longest Circular Road（★4）
# https://atcoder.jp/contests/typical90/tasks/typical90_c
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/003.cpp

from queue import Queue
INF = 1<<30

def getdist(start):
    # 幅優先探索（BFS）により、最短距離を計算
    Q = Queue()
    Q.put(start)
    dist[start] = 0
    while not Q.empty():
        pos = Q.get()
        for to in G[pos]:
            if dist[to] == INF:
                dist[to] = dist[pos] + 1
                Q.put(to)

# Step #1. 入力
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

# Step #2. 頂点 1 からの最短距離を求める
# maxid1: 頂点 1 から最も離れている（最短距離が長い）頂点
dist = [INF] * N
getdist(0)
maxn1 = -1
maxid1 = -1
for i in range(N):
    if maxn1 < dist[i]:
        maxn1 = dist[i]
        maxid1 = i

# Step #3. 頂点 maxid1 からの最短距離を求める
# maxn2: 木の直径（最短距離の最大値）
dist = [INF] * N
getdist(maxid1)
maxn2 = -1
for i in range(N):
    maxn2 = max(maxn2, dist[i])

# Step #4. 出力
print(maxn2 + 1)