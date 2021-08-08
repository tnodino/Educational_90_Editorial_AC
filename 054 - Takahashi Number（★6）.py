# 054 - Takahashi Number（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_bb
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/054.cpp

from queue import Queue

N,M = map(int,input().split())
G = [[] for _ in range(N+M)]
for i in range(M):
    k = int(input())
    v = list(map(int,input().split()))
    for j in range(k):
        v[j] -= 1
        G[v[j]].append(N+i)
        G[N+i].append(v[j])
que = Queue()
que.put(0)
dist = [-2] * (N+M)
dist[0] = 0
while not que.empty():
    u = que.get()
    for i in G[u]:
        if dist[i] == -2:
            dist[i] = dist[u] + 1
            que.put(i)
for i in range(N):
    print(dist[i] // 2)