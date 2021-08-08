# 089 - Partitions and Inversions（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_ck
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/089-04.cpp

mod = 10**9+7

# Step #1. Input
N,K = map(int,input().split())
A = list(map(int,input().split()))

# Step #2. Maeshori
cl = [0] * N
l = N - 1
cnt = 0
for r in range(N-1,-1,-1):
    while l >= 0 and cnt <= K:
        l -= 1
        for i in range(l+1,r+1):
            if A[l] > A[i]:
                cnt += 1
    cl[r] = l + 1
    for i in range(l,r):
        if A[i] > A[r]:
            cnt -= 1

# Step #3. DP
dp = [0] * (N+1)
dp[0] = 1
for i in range(1,N+1):
    for j in range(cl[i-1],i):
        dp[i] += dp[j]
        dp[i] %= mod
print(dp[N])
