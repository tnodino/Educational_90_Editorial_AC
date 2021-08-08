# 090 - Tenkei90's Last Problem（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_cl
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/090-01.cpp

mod = 998244353

N,K = map(int,input().split())
dp = [[[0] * (N+1) for __ in range(N)] for _ in range(K+1)]
# dp[h][l][r]: 配列の区間 (A[l], A[l+1], ..., A[r-1]) で、すべて A[i] >= h であるものの個数
for h in range(K,-1,-1):
    for i in range(N):
        dp[h][i][i] = 1
for h in range(K,-1,-1):
    for l in range(N):
        for r in range(l+1,N+1):
            if h * (r - l) > K:
                continue
            dp[h][l][r] = dp[h][l][r-1]
            if h != K:
                for i in range(l,r):
                    dp[h][l][r] = (dp[h][l][r] + dp[h+1][i][r] * dp[h][l][i-1 if i != l else l]) % mod
print(dp[0][0][N])