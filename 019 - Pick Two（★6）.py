# 019 - Pick Two（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_s
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/019.cpp

# Step #1. Input
N = int(input())
A = list(map(int,input().split()))

# Step #2. Initialize
dp = [[1<<29] * (2*N) for _ in range(2*N)]
for i in range(2*N):
    if i < 2 * N - 1:
        dp[i][i+1] = abs(A[i] - A[i+1])

# Step #3. DP
for i in range(1,2*N,2):
    for j in range(2*N-i):
        cl = j; cr = j + i
        for k in range(cl,cr):
            dp[cl][cr] = min(dp[cl][cr], dp[cl][k] + dp[k+1][cr])
        dp[cl][cr] = min(dp[cl][cr], dp[cl+1][cr-1] + abs(A[cl] - A[cr]))

# Step #4. Output
print(dp[0][2*N-1])