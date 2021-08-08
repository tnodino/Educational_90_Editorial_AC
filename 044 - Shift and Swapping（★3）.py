# 044 - Shift and Swapping（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_ar
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/044.cpp

N,Q = map(int,input().split())
A = list(map(int,input().split()))
shifts = 0
for _ in range(Q):
    T,x,y = map(int,input().split())
    if T == 1:
        x -= 1
        y -= 1
        A[(x + shifts) % N],A[(y + shifts) % N] = A[(y + shifts) % N],A[(x + shifts) % N]
    if T == 2:
        shifts = (shifts + N - 1) % N
    if T == 3:
        x -= 1
        print(A[(x + shifts) % N])