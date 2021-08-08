# 062 - Paint All（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_bj
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/062.cpp

from queue import Queue

# Step #1. 入力
N = int(input())
G = [[] for _ in range(N)]
usable = [False] * N
Q = Queue()
for i in range(N):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(i)
    G[b].append(i)
    if a == i or b == i:
        usable[i] = True
        Q.put(i)

# Step #2. 後ろからシミュレーション
vec = []
while not Q.empty():
    pos = Q.get()
    vec.append(pos)
    for i in G[pos]:
        if usable[i] == True:
            continue
        usable[i] = True
        Q.put(i)

# Step #3. 答えを求める
vec.reverse()
if len(vec) != N:
    print(-1)
else:
    for i in range(len(vec)):
        print(vec[i] + 1)