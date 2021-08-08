# 061 - Deck（★2）
# https://atcoder.jp/contests/typical90/tasks/typical90_bi
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/061-01.cpp

# Step #1. 入力
Q = int(input())
_L = [list(map(int,input().split())) for _ in range(Q)]
T,X = [list(i) for i in zip(*_L)]

# Step #2. 答えを求める
cl = 500000
cr = 500000
A = [0] * (1000000)
for i in range(Q):
    if T[i] == 1:
        cl -= 1
        A[cl] = X[i]
    if T[i] == 2:
        A[cr] = X[i]
        cr += 1
    if T[i] == 3:
        print(A[cl+X[i]-1])