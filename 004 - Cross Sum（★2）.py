# 004 - Cross Sum（★2）
# https://atcoder.jp/contests/typical90/tasks/typical90_d
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/004.cpp

# Step #1. 入力
H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

# Step #2. 前計算
Row = [0] * H
Column = [0] * W
for i in range(H):
    for j in range(W):
        Row[i] += A[i][j]
        Column[j] += A[i][j]

# Step #3. 答えの計算
Answer = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        Answer[i][j] = Row[i] + Column[j] - A[i][j]

# Step #4. 出力
for i in range(H):
    print(*Answer[i])