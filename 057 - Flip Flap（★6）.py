# 057 - Flip Flap（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_be
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/057.cpp

mod = 998244353

N,M = map(int,input().split())
D = [[0] * M for _ in range(N)]
for i in range(N):
    t = int(input())
    x = list(map(int,input().split()))
    for j in range(t):
        D[i][x[j]-1] = 1
S = list(map(int,input().split()))
pos = 0
for i in range(M):
    found = False
    for j in range(pos,N):
        if D[j][i] == 1:
            if j != pos:
                D[j],D[pos] = D[pos],D[j]
            found = True
            break
    if found:
        for j in range(N):
            if j != pos and D[j][i] == 1:
                for k in range(i,M):
                    D[j][k] ^= D[pos][k]
        if S[i] == 1:
            for j in range(i,M):
                S[j] ^= D[pos][j]
        pos += 1
if S == [0] * M:
    ans = pow(2, N-pos, mod)
    print(ans)
else:
    print(0)