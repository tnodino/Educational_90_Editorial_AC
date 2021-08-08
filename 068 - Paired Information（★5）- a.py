# 068 - Paired Information（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_bp
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/068a.cpp

from sys import setrecursionlimit
setrecursionlimit(10**6)

class union_find:
    def __init__(self, N):
        self.N = N
        self.par = [0] * N
        for i in range(N):
            self.par[i] = i

    def root(self, x):
        if x == self.par[x]: return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def link(self, x, y):
        self.par[self.root(x)] = self.root(y)

    def connected(self, x, y):
        return self.root(x) == self.root(y)

N = int(input())
Q = int(input())
_L = [list(map(int,input().split())) for _ in range(Q)]
T,X,Y,V = [list(i) for i in zip(*_L)]
for i in range(Q):
    X[i] -= 1
    Y[i] -= 1
_sum = [0] * (N-1)
for i in range(Q):
    if T[i] == 0:
        _sum[X[i]] = V[i]
potential = [0] * N
for i in range(N - 1):
    potential[i + 1] = _sum[i] - potential[i]
uf = union_find(N)
for i in range(Q):
    if T[i] == 0:
        uf.link(X[i], Y[i])
    if T[i] == 1:
        if not uf.connected(X[i], Y[i]):
            print('Ambiguous')
        elif (X[i] + Y[i]) % 2 == 0:
            print(V[i] + (potential[Y[i]] - potential[X[i]]))
        else:
            print((potential[X[i]] + potential[Y[i]]) - V[i])