# 071 - Fuzzy Priority（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_bs
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/071-02.cpp

from queue import Queue

N,M,K = map(int,input().split())
assert(K == 1)
G = [[] for _ in range(N)]
deg = [0] * N
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    deg[b] += 1
que = Queue()
for i in range(N):
    if deg[i] == 0:
        que.put(i)
perm = []
while not que.empty():
    u = que.get()
    perm.append(u)
    for i in G[u]:
        deg[i] -= 1
        if deg[i] == 0:
            que.put(i)
if len(perm) != N:
    print(-1)
else:
    for i in range(N):
        perm[i] += 1
    print(*perm)