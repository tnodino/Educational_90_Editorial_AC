# 005 - Restricted Digits（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_e
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/005-03.cpp

mod = 10**9+7

# Step #1. 入力
N,B,K = map(int,input().split())
C = list(map(int,input().split()))

# Step #2. 前計算
power10 = [0] * 64
for i in range(63):
    power10[i] = pow(10, 1<<i, B)

# Step #3. dp[1][i] を求める
dp = [[0] * B for _ in range(64)]
for i in range(K):
    dp[0][C[i] % B] += 1

# Step #4. dp[1][i], dp[2][i], ..., dp[2^n][i] を求める
for i in range(62):
    for j in range(B):
        for k in range(B):
            nex = (j * power10[i] + k) % B
            dp[i+1][nex] += dp[i][j] * dp[i][k]
            dp[i+1][nex] %= mod

# Step #5. 繰り返し二乗法により dp[N][i] を求める
Answer = [[0] * B for _ in range(64)]
Answer[0][0] = 1
for i in range(62):
    if N & (1 << i) != 0:
        for j in range(B):
            for k in range(B):
                nex = (j * power10[i] + k) % B
                Answer[i+1][nex] += Answer[i][j] * dp[i][k]
                Answer[i+1][nex] %= mod
    else:
        for j in range(B):
            Answer[i+1][j] = Answer[i][j]

# Step #6. 出力
print(Answer[62][0])