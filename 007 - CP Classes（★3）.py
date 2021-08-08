# 007 - CP Classes（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_g
#https://github.com/E869120/kyopro_educational_90/blob/main/sol/007.cpp

from bisect import bisect_left
INF = 10**10

# Step #1. Input
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
B = list(int(input()) for _ in range(Q))

# Step #2. Sorting
A.sort()

# Step #3. Binary Search
for i in range(Q):
    pos1 = bisect_left(A, B[i])
    Diff1 = INF
    Diff2 = INF
    if pos1 < N:
        Diff1 = abs(B[i] - A[pos1])
    if 0 < pos1:
        Diff2 = abs(B[i] - A[pos1-1])
    print(min(Diff1, Diff2))