# 056 - Lucky Bag（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_bd
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/056.cpp

N,S = map(int,input().split())
A,B = [],[]
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
dp = [[False] * (S+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    for j in range(S+1):
        if j >= A[i] and dp[i][j-A[i]]:
            dp[i+1][j] = True
        if j >= B[i] and dp[i][j-B[i]]:
            dp[i+1][j] = True
if not dp[N][S]:
    print('Impossible')
else:
    res = ['?'] * N
    pos = S
    for i in range(N-1,-1,-1):
        if pos >= B[i] and dp[i][pos-B[i]]:
            res[i] = 'B'
            pos -= B[i]
        else:
            res[i] = 'A'
            pos -= A[i]
    print(''.join(res))