# 089 - Partitions and Inversions（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_ck
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/089-05.cpp

from bisect import bisect_left
mod = 10**9+7

class BIT:
    def __init__(self, sz):
        self.size_ = sz + 2
        self.bit = [0] * (self.size_ + 2)

    def add(self, pos, x):
        pos += 1
        while pos <= self.size_:
            self.bit[pos] += x
            pos += (pos & -pos)

    def sum(self, pos):
        s = 0
        pos += 1
        while pos >= 1:
            s += self.bit[pos]
            pos -= (pos & -pos)
        return s

# Step #1. Input
N,K = map(int,input().split())
A = list(map(int,input().split()))

# Step #2. Coordinate Compression
V = set()
for i in range(N):
    V.add(A[i])
V = list(V)
V.sort()
for i in range(N):
    A[i] = bisect_left(V, A[i])

# Step #3. Maeshori
cl = [0] * N
l = N - 1
cnt = 0
Z = BIT(len(V) + 2)
Z.add(A[N-1], 1)
for r in range(N-1,-1,-1):
    while l >= 0 and cnt <= K:
        l -= 1
        cnt += Z.sum(A[l] - 1)
        Z.add(A[l], 1)
    Z.add(A[r], -1)
    cnt -= (Z.sum(len(V) + 1) - Z.sum(A[r]))
    cl[r] = l + 1

# Step #4. DP
dp = [0] * (N+1)
ru = [0] * (N+1)
dp[0] = 1
ru[0] = 1
for i in range(1,N+1):
    if cl[i-1] == 0:
        dp[i] = ru[i-1]
    if cl[i-1] >= 1:
        dp[i] = (ru[i-1] - ru[cl[i-1]-1] + mod) % mod
    ru[i] = (ru[i-1] + dp[i]) % mod
print(dp[N])