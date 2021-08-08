# 005 - Restricted Digits（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_e
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/005-01.cpp

mod = 10**9+7

# Step #1. 入力
N,B,K = map(int,input().split())
C = list(map(int,input().split()))

# Step #2. 動的計画法
dp = [[0] * B for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(B):
        for k in range(K):
            nex = (10 * j + C[k]) % B
            dp[i+1][nex] += dp[i][j]
            dp[i+1][nex] %= mod

# Step #3. 出力
print(dp[N][0])