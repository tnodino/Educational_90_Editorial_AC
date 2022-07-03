# 072 - Loop Railway Plan（★4）
# https://atcoder.jp/contests/typical90/tasks/typical90_bt
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/072.cpp

from sys import setrecursionlimit
setrecursionlimit(10**6)

def dfs(sx, sy, px, py):
    if sx == px and sy == py and used[px][py] == True:
        return 0
    used[px][py] = True
    ret = -10000
    for i in range(4):
        nx = px + dx[i]
        ny = py + dy[i]
        if nx < 0 or ny < 0 or nx >= H or ny >= W or c[nx][ny] == '#':
            continue
        if (sx != nx or sy != ny) and used[nx][ny] == True:
            continue
        v = dfs(sx, sy, nx, ny)
        ret = max(ret, v + 1)
    used[px][py] = False
    return ret

# Step #1. Input
H,W = map(int,input().split())
c = [list(input()) for _ in range(H)]

# Step #2. DFS
dx = [ 0, 1, 0,-1]
dy = [ 1, 0,-1, 0]
used = [[False] * 20 for _ in range(20)]
Answer = -1
for i in range(H):
    for j in range(W):
        Answer = max(Answer, dfs(i, j, i, j))
if Answer <= 2:
    Answer = -1
print(Answer)