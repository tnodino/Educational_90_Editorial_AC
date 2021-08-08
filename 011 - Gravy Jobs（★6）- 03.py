# 011 - Gravy Jobs（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_k
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/011-01.cpp

# Step #1. 入力
# Step #2. D[i] の昇順にソート
N = int(input())
_L = [list(map(int,input().split())) for _ in range(N)]
_L.sort()
D,C,S = [list(i) for i in zip(*_L)]

# Step #3. 動的計画法
dp = [[0] * (5001) for _ in range(N+1)]
for i in range(N):
    for j in range(5001):
        # 仕事 i + 1 をやらない場合
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        # 仕事 i + 1 をやる場合
        if j + C[i] <= D[i]:
            dp[i+1][j+C[i]] = max(dp[i+1][j+C[i]], dp[i][j] + S[i])

# Step #4. 出力
Answer = 0
for i in range(5001):
    Answer = max(Answer, dp[N][i])
print(Answer)