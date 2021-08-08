# 083 - Colorful Graph（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_ce
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/083-01.cpp

N,M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
Q = int(input())
col = [1] * N
for _ in range(Q):
    x,y = map(int,input().split())
    x -= 1
    print(col[x])
    col[x] = y
    for j in G[x]:
        col[j] = y