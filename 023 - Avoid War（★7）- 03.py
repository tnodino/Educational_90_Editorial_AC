# 023 - Avoid War（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_w
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/023-03.cpp

mod = 10**9+7

# Step #1. Input
H,W = map(int,input().split())
c = [list(input()) for _ in range(H)]

# Step #2. DP
dp = [[[0] * (1<<(W+1)) for __ in range(W)] for _ in range(H+1)]
dp[0][0][0] = 1
for i in range(H):
    for j in range(W):
        n1 = i
        n2 = j + 1
        if n2 == W:
            n1 += 1
            n2 = 0
        for k in range(1<<(W+1)):
            if dp[i][j][k] == 0:
                continue
            bit = [0] * 18
            for l in range(W+1):
                bit[l] = (k // (1 << l)) % 2
            dp[n1][n2][k >> 1] += dp[i][j][k]
            dp[n1][n2][k >> 1] %= mod
            flag = True
            if c[i][j] == '#':
                flag = False
            if bit[0] == 1 and i >= 1 and j >= 1:
                flag = False
            if bit[1] == 1 and 1 >= 1:
                flag = False
            if bit[2] == 1 and i >= 1 and j <= W - 2:
                flag = False
            if bit[W] == 1 and j >= 1:
                flag = False
            if flag == True:
                dp[n1][n2][(k>>1) + (1<<W)] += dp[i][j][k]
                dp[n1][n2][(k>>1) + (1<<W)] %= mod

# Step #3. Get Answer
Answer = 0
for i in range(1<<(W+1)):
    Answer += dp[H][0][i]
print(Answer % mod)