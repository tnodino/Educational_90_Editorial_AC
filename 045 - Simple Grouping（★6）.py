# 045 - Simple Grouping（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_as
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/045.cpp

N,K = map(int,input().split())
_L = [list(map(int,input().split())) for _ in range(N)]
X,Y = [list(i) for i in zip(*_L)]
d = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        d[i][j] = pow(X[i]-X[j], 2) + pow(Y[i]-Y[j], 2)
cost = [0] * (1<<N)
for i in range(1,1<<N):
    for j in range(N):
        for k in range(j):
            if (i >> j) & 1 == 1 and (i >> k) & 1 == 1:
                cost[i] = max(cost[i], d[j][k])
dp = [[10**18] * (1<<N) for _ in range(K+1)]
dp[0][0] = 0
for i in range(1,K+1):
    for j in range(1,1<<N):
        k = j
        while k != 0:
            dp[i][j] = min(dp[i][j], max(dp[i-1][j-k], cost[k]))
            k = (k - 1) & j
print(dp[K][(1<<N)-1])