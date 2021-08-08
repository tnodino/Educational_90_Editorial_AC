# 023 - Avoid War（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_w
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/023-02.cpp

mod = 10**9+7

# Step #1. Input
H,W = map(int,input().split())
c = [list(input()) for _ in range(H)]

# Step #2. DP
dp = [[0] * (1<<W) for _ in range(H+1)]
dp[0][0] = 1
for i in range(H):
    for j in range(1<<W):
        if dp[i][j] == 0:
            continue
        for k in range(1<<W):
            bit = [[0] * W for _ in range(2)]
            flag = False
            for l in range(W):
                bit[0][l] = (j // (1 << l)) % 2
            for l in range(W):
                bit[1][l] = (k // (1 << l)) % 2
            for l in range(W):
                if bit[0][l] == 1 and bit[1][l] == 1:
                    flag = True
                if l < W - 1 and bit[1][l] == 1 and bit[1][l+1] == 1:
                    flag = True
                if l < W - 1 and bit[0][l] == 1 and bit[1][l+1] == 1:
                    flag = True
                if l < W - 1 and bit[1][l] == 1 and bit[0][l+1] == 1:
                    flag = True
                if bit[1][l] == 1 and c[i][l] == '#':
                    flag = True
            if flag == False:
                dp[i+1][k] += dp[i][j]
                dp[i+1][k] %= mod

# Step #3. Output
Answer = 0
for i in range(1<<W):
    Answer += dp[H][i]
print(Answer % mod)