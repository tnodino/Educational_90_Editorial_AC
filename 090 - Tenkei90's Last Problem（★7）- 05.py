# 090 - Tenkei90's Last Problem（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_cl
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/090-05.cpp

mod = 998244353

N,K = map(int,input().split())
dp = [[] for _ in range(K+1)]
dp[K] = [0, 1]
for i in range(K-1,-1,-1):
    limit = N if i == 0 else min(K // i, N)
    dp[i] = [0] * (limit+1)
    for j in range(1,limit+1):
        dp[i][j] = dp[i][j-1] if j != 1 else 1
        for k in range(2,len(dp[i+1])+1):
            if k > j + 1:
                break
            dp[i][j] = (dp[i][j] + dp[i+1][k-1] * (dp[i][j-k] if k < j else 1)) % mod
print(dp[0][N])