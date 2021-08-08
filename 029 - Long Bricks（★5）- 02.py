# 029 - Long Bricks（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_ac
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/029-02.cpp

from bisect import bisect_left

W,N = map(int,input().split())
L,R = [], []
for i in range(N):
    l,r = map(int,input().split())
    l -= 1
    L.append(l)
    R.append(r)
compression = set()
for i in range(N):
    compression.add(L[i])
    compression.add(R[i])
compression = list(compression)
compression.sort()
for i in range(N):
    L[i] = bisect_left(compression, L[i])
    R[i] = bisect_left(compression, R[i])
h = [0] * (len(compression)+1)
for i in range(N):
    height = max(h[L[i]:R[i]]) + 1
    for j in range(L[i],R[i]):
        h[j] = height
    print(height)