# 060 - Chimera（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_bh
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/060.cpp

from bisect import bisect_left
INF = 10**6

# Step #1. 入力
N = int(input())
A = list(map(int,input().split()))

# Step #2. 左側の LIS を求める
P = [0] * N
dp = [INF] * N
for i in range(N):
    pos1 = bisect_left(dp, A[i])
    dp[pos1] = A[i]
    P[i] = pos1 + 1

# Step #3. 右側の LIS を求める
Q = [0] * N
dp = [INF] * N
for i in range(N-1,-1,-1):
    pos1 = bisect_left(dp, A[i])
    dp[pos1] = A[i]
    Q[i] = pos1 + 1

# Step #4. 答えを求める
Answer = 0
for i in range(N):
    Answer = max(Answer, P[i] + Q[i] - 1)
print(Answer)