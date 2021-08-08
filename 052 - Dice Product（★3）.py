# 052 - Dice Product（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_az
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/052.cpp

mod = 10**9+7

# Step #1. 入力
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

# Step #2. 答えを求める
Answer = 1
for i in range(N):
    Answer *= sum(A[i])
    Answer %= mod
print(Answer)