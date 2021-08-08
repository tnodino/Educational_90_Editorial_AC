# 021 - Come Back in One Piece（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_u
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/021.cpp

from sys import setrecursionlimit
setrecursionlimit(10**6)

def dfs(pos):
    used[pos] = True
    for i in G[pos]:
        if used[i] == False:
            dfs(i)
    I.append(pos)

def dfs2(pos):
    global cnts
    used[pos] = True
    cnts += 1
    for i in H[pos]:
        if used[i] == False:
            dfs2(i)

# Step #1. Input
N,M = map(int,input().split())
G = [[] for _ in range(N)]
H = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    H[b].append(a)

# Step #2. First DFS
I = []
used = [False] * N
for i in range(N):
    if used[i] == False:
        dfs(i)

# Step #3. Second DFS
Answer = 0
I.reverse()
used = [False] * N
for i in I:
    if used[i] == True:
        continue
    cnts = 0
    dfs2(i)
    Answer += cnts * (cnts - 1) // 2

# Step #4. Output The Answer!
print(Answer)