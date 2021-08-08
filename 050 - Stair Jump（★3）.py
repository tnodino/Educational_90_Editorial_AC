# 050 - Stair Jump（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_ax
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/049.cpp

mod = 10**9+7

# Step #1. Input
N,L = map(int,input().split())

# Step #2. DP
dp = [0] * (N+1)
dp[0] = 1
for i in range(1,N+1):
    if i < L:
        dp[i] = dp[i-1]
    else:
        dp[i] = (dp[i-1] + dp[i-L]) % mod

# Step #3. Output
print(dp[N])