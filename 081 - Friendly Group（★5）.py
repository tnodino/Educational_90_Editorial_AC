# 081 - Friendly Group（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_cc
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/081.cpp

N,K = map(int,input().split())
_L = [list(map(int,input().split())) for _ in range(N)]
A,B = [list(i) for i in zip(*_L)]
R = max(max(A) ,K) + 1
C = max(max(B) ,K) + 1
_sum = [[0] * (C+1) for _ in range(R+1)]
for i in range(N):
    _sum[A[i]+1][B[i]+1] += 1
for i in range(1,R+1):
    for j in range(1,C+1):
        _sum[i][j] += _sum[i-1][j]
for i in range(1,R+1):
    for j in range(1,C+1):
        _sum[i][j] += _sum[i][j-1]
answer = 0
for i in range(R-K):
    for j in range(C-K):
        answer = max(answer, _sum[i][j] + _sum[i+K+1][j+K+1] - _sum[i][j+K+1] - _sum[i+K+1][j])
print(answer)