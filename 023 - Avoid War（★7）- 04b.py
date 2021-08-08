# 023 - Avoid War（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_w
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/023-04b.cpp

from sys import setrecursionlimit
setrecursionlimit(50)

from collections import defaultdict
mod = 10**9+7

def hantei(sx, sy):
    dx = [-1,-1,-1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0,-1,-1]
    for i in range(8):
        tx = sx + dx[i]
        ty = sy + dy[i]
        if tx < 0 or ty < 0 or ty >= W:
            continue
        if used[tx][ty] == True:
            return False
    return True

def dfs(pos, dep, str):
    sx = pos // W; sy = pos % W
    if dep == W + 1:
        idx = cnt[sy]
        flag = hantei(sx, sy)
        state[sy][idx] = str
        Map[sy][str] = (idx, flag)
        cnt[sy] += 1
        return
    dfs(pos+1, dep+1, str)
    if hantei(sx, sy) == True:
        used[sx][sy] = True
        dfs(pos+1, dep+1, str + (1<<dep))
        used[sx][sy] = False

# Step #1. Input
H,W = map(int,input().split())
c = [list(input()) for _ in range(H)]

# Step #2. Initialize
cnt = [0] * W
used = [[False] * (W+10) for _ in range(H+10)]
state = [[0] * (1<<18) for _ in range(W)]
Map = [defaultdict(int) for _ in range(W)]
for i in range(W):
    dfs(i, 0, 0)
nex0 = [[0] * (1<<18) for _ in range(W)]
nex1 = [[0] * (1<<18) for _ in range(W)]
for i in range(W):
    for j in range(cnt[i]):
        t = state[i][j]
        t0 = (t >> 1)
        t1 = (t >> 1) + (1 << W)
        if t0 in Map[(i+1) % W]:
            nex0[i][j] = Map[(i+1) % W][t0][0]
        if t1 in Map[(i+1) % W] and Map[i][t][1] == True:
            nex1[i][j] = Map[(i+1) % W][t1][0]
        else:
            nex1[i][j] = -1

# Step #3. DP
dp = [[0] * (1<<18) for _ in range(W)]
dp[0][0] = 1
for i in range(H):
    dp2 = [[0] * (1<<18) for _ in range(W)]
    for j in range(W):
        n2 = j + 1
        if n2 == W:
            n2 = 0
        for k in range(cnt[j]):
            if dp[j][k] == 0:
                continue
            if n2 > 0:
                dp[n2][nex0[j][k]] += dp[j][k]
                dp[n2][nex0[j][k]] %= mod
            else:
                dp2[n2][nex0[j][k]] += dp[j][k]
                dp2[n2][nex0[j][k]] %= mod
            if nex1[j][k] != -1 and c[i][j] == '.':
                if n2 > 0:
                    dp[n2][nex1[j][k]] += dp[j][k]
                    dp[n2][nex1[j][k]] %= mod
                else:
                    dp2[n2][nex1[j][k]] += dp[j][k]
                    dp2[n2][nex1[j][k]] %= mod
    dp = dp2

# Step #4. Output The Answer
Answer = 0
for i in range(cnt[0]):
    Answer += dp[0][i]
    Answer %= mod
print(Answer)