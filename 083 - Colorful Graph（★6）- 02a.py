# 083 - Colorful Graph（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_ce
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/083-02a.cpp

from math import sqrt

N,M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
Q = int(input())
X,Y = [],[]
for _ in range(Q):
    x,y = map(int,input().split())
    x -= 1
    X.append(x)
    Y.append(y)
B = int(sqrt(2 * M))
large = []
for i in range(N):
    if len(G[i]) >= B:
        large.append(i)
link = [[False] * len(large) for _ in range(N)]
for i in range(len(large)):
    for j in G[large[i]]:
        link[j][i] = True
    link[large[i]][i] = True
update = [-1] * N
update_large = [-1] * len(large)
for i in range(Q):
    last = update[X[i]]
    for j in range(len(large)):
        if link[X[i]][j]:
            last = max(last, update_large[j])
    print(Y[last] if last != -1 else 1)
    if len(G[X[i]]) < B:
        update[X[i]] = i
        for j in G[X[i]]:
            update[j] = i
    else:
        ptr = -1
        for j in range(len(large)):
            if large[j] == X[i]:
                ptr = j
                break
        update_large[ptr] = i