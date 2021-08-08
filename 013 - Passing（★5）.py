# 013 - Passing（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_m
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/013.cpp

from heapq import heappush, heappop

def dijkstra(stt):
    Q = []
    dist = [1<<60] * N
    dist[stt] = 0
    heappush(Q, (0, stt))
    while Q:
        pos = heappop(Q)[1]
        for i in range(len(G[pos])):
            to = G[pos][i][0]
            cost = G[pos][i][1]
            if dist[to] > dist[pos] + cost:
                dist[to] = dist[pos] + cost
                heappush(Q, (dist[to], to))
    return dist

# Step #1. 入力
N,M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append((b, c))
    G[b].append((a, c))

# Step #2. 頂点 1 からの最短距離を求める
dist1 = dijkstra(0)

# Step #3. 頂点 N からの最短距離を求める
distN = dijkstra(N-1)

# Step #4. 出力
for i in range(N):
    Answer = dist1[i] + distN[i]
    print(Answer)