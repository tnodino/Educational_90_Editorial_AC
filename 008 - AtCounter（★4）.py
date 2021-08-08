# 008 - AtCounter（★4）
# https://atcoder.jp/contests/typical90/tasks/typical90_h
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/008.cpp

mod = 10**9+7

# Step #1. Input
N = int(input())
S = input()

# Step #2. Dynamic Programming (DP)
dp = [[0] * 8 for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(8):
        dp[i+1][j] += dp[i][j]
        if S[i] == 'a' and j == 0:
            dp[i+1][j+1] += dp[i][j]
        if S[i] == 't' and j == 1:
            dp[i+1][j+1] += dp[i][j]
        if S[i] == 'c' and j == 2:
            dp[i+1][j+1] += dp[i][j]
        if S[i] == 'o' and j == 3:
            dp[i+1][j+1] += dp[i][j]
        if S[i] == 'd' and j == 4:
            dp[i+1][j+1] += dp[i][j]
        if S[i] == 'e' and j == 5:
            dp[i+1][j+1] += dp[i][j]
        if S[i] == 'r' and j == 6:
            dp[i+1][j+1] += dp[i][j]
    for j in range(8):
        dp[i+1][j] %= mod

# Step #3. Output the answer
print(dp[N][7])