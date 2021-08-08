# 073 - We Need Both a and b（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_bu
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/073.cpp

mod = 10**9+7

def dfs(pos, pre):
    val1 = 1
    val2 = 1
    for i in G[pos]:
        if i == pre:
            continue
        dfs(i, pos)
        if C[pos] == 'a':
            val1 *= dp[i][0] + dp[i][2]
            val2 *= dp[i][0] + dp[i][1] + 2 * dp[i][2]
        if C[pos] == 'b':
            val1 *= dp[i][1] + dp[i][2]
            val2 *= dp[i][0] + dp[i][1] + 2 * dp[i][2]
        val1 %= mod
        val2 %= mod
    if C[pos] == 'a':
        dp[pos][0] = val1
        dp[pos][2] = (val2 - val1 + mod) % mod
    if C[pos] == 'b':
        dp[pos][1] = val1
        dp[pos][2] = (val2 - val1 + mod) % mod

# Step #1. Input
N = int(input())
C = list(input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

# Step #2. DFS
dp = [[0] * 3 for _ in range(N)]
dfs(0, -1)
print(dp[0][2])