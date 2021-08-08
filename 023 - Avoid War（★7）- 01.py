# 023 - Avoid War（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_w
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/023-01.cpp

def hantei(sx, sy):
    dx = [-1,-1,-1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0,-1,-1]
    for i in range(8):
        tx = sx + dx[i]
        ty = sy + dy[i]
        if tx < 0 or ty < 0 or tx >= H or ty >= W:
            continue
        if used[tx][ty] == True:
            return False
    return True

def dfs(sx, sy):
    if sx == H:
        return 1
    nx = sx
    ny = sy + 1
    if ny == W:
        nx += 1
        ny = 0
    ret1 = dfs(nx, ny)
    ret2 = 0
    if hantei(sx, sy) == True and c[sx][sy] == '.':
        used[sx][sy] = True
        ret2 = dfs(nx, ny)
        used[sx][sy] = False
    return ret1 + ret2

# Step #1. Input
H,W = map(int,input().split())
c = [list(input()) for _ in range(H)]

# Step #2. DFS
used = [[False] * W for _ in range(H)]
Answer = dfs(0, 0)
print(Answer)