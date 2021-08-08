# 036 - Max Manhattan Distance（★5
# https://atcoder.jp/contests/typical90/tasks/typical90_aj
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/036.cpp

INF = 1<<60

# Step #1. 入力
N,Q = map(int,input().split())
_L = [list(map(int,input().split())) for _ in range(N)]
X,Y = [list(i) for i in zip(*_L)]
T = []
for _ in range(Q):
    t = int(input())
    T.append(t-1)

# Step #2. 45 度回転
min_X = INF
max_X = -INF
min_Y = INF
max_Y = -INF
for i in range(N):
    p1 = X[i] + Y[i]
    p2 = Y[i] - X[i]
    X[i] = p1
    Y[i] = p2
    min_X = min(min_X, X[i])
    max_X = max(max_X, X[i])
    min_Y = min(min_Y, Y[i])
    max_Y = max(max_Y, Y[i])

# Step #3. クエリに答える
for i in range(Q):
    ret1 = abs(X[T[i]] - min_X)
    ret2 = abs(X[T[i]] - max_X)
    ret3 = abs(Y[T[i]] - min_Y)
    ret4 = abs(Y[T[i]] - max_Y)
    print(max(ret1, ret2, ret3, ret4))