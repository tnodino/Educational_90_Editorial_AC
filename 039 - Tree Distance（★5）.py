# 039 - Tree Distance（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_am
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/039.cpp

from sys import setrecursionlimit
setrecursionlimit(10**6)

def dfs(pos, pre):
    dp[pos] = 1
    for i in G[pos]:
        if i == pre:
            continue
        dfs(i, pos)
        dp[pos] += dp[i]

# Step #1. 入力
N = int(input())
A,B = [],[]
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    A.append(a)
    B.append(b)
    G[a].append(b)
    G[b].append(a)

# Step #2. 深さ優先探索（DFS）
dp = [0] * N
dfs(0, -1)

# Step #3. 答えを求める
Answer = 0
for i in range(N-1):
    r = min(dp[A[i]], dp[B[i]])
    Answer += r * (N - r)
print(Answer)