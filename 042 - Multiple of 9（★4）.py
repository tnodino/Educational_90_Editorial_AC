# 042 - Multiple of 9（★4）
# https://atcoder.jp/contests/typical90/tasks/typical90_ap
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/042.cpp

mod = 10**9+7

K = int(input())
if K % 9 == 0:
    dp = [0] * (K+1)
    dp[0] = 1
    for i in range(1,K+1):
        for j in range(i - 1, -1, -1):
            if j < i - 9: break
            dp[i] += dp[j]
            if dp[i] >= mod: dp[i] -= mod
    print(dp[K])
else:
    print(0)