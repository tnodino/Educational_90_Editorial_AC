# 090 - Tenkei90's Last Problem（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_cl
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/090-01.cpp

mod = 998244353

N,K = map(int,input().split())
dp = [[0] * 2 for _ in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % mod
    dp[i][1] = dp[i-1][0]
answer = (dp[N][0] + dp[N][1]) % mod
print(answer)