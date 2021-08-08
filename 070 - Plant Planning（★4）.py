# 070 - Plant Planning（★4）
# https://atcoder.jp/contests/typical90/tasks/typical90_br
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/070.cpp

N = int(input())
_L = [list(map(int,input().split())) for _ in range(N)]
X,Y = [list(i) for i in zip(*_L)]
X.sort()
Y.sort()
ans = 0
for i in range(N):
    ans += abs(X[i] - X[N//2])
    ans += abs(Y[i] - Y[N//2])
print(ans)