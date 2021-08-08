# 028 - Cluttered Paper（★4）
# https://atcoder.jp/contests/typical90/tasks/typical90_ab
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/028.cpp

# Step #1. Input
N = int(input())
_L = [list(map(int,input().split())) for _ in range(N)]
lx,ly,rx,ry = [list(i) for i in zip(*_L)]

# Step #2. Imos Method in 2D
cnt = [[0] * (1001) for _ in range(1001)]
for i in range(N):
    cnt[lx[i]][ly[i]] += 1
    cnt[lx[i]][ry[i]] -= 1
    cnt[rx[i]][ly[i]] -= 1
    cnt[rx[i]][ry[i]] += 1
for i in range(1001):
    for j in range(1001):
        cnt[i][j] += cnt[i][j-1]
for i in range(1001):
    for j in range(1001):
        cnt[i][j] += cnt[i-1][j]

# Step #3. Count Number
Answer = [0] * (N+1)
for i in range(1001):
    for j in range(1001):
        if cnt[i][j] >= 1:
            Answer[cnt[i][j]] += 1

# Step #4. Output The Answer
for i in range(1,N+1):
    print(Answer[i])