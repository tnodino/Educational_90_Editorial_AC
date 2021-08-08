# 029 - Long Bricks（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_ac
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/029-01.cpp

W,N = map(int,input().split())
A = [0] * (W+1)
for _ in range(N):
    L,R = map(int,input().split())
    height = max(A[L:R+1]) + 1
    for i in range(L,R+1):
        A[i] = height
    print(height)