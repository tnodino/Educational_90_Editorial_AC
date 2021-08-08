# 089 - Partitions and Inversions（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_ck
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/089-03.cpp

mod = 10**9+7

# Step #1. Input
N,K = map(int,input().split())
A = list(map(int,input().split()))

# Step #2. Maeshori
cl = [0] * N
for i in range(N):
    cnt = 0
    for j in range(i-1,-1,-1):
        for k in range(j+1,i+1):
            if A[j] > A[k]:
                cnt += 1
            if cnt > K:
                cl[i] = j + 1
                break
        if cnt > K:
            break

# Step #3. DP
dp = [0] * (N+1)
dp[0] = 1
for i in range(1,N+1):
    for j in range(cl[i-1],i):
        dp[i] += dp[j]
        dp[i] %= mod
print(dp[N])