# 005 - Restricted Digits（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_e
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/005-02.cpp

mod = 10**9+7

class Matrix():
    def __init__(self, sz):
        self.sz = sz # sz × sz 行列
        self.x = [[0] * sz for _ in range(sz)]

def multiply(A, B):
    # A × B を求める
    C = Matrix(A.sz)
    for i in range(A.sz):
        for j in range(A.sz):
            for k in range(A.sz):
                C.x[i][k] += A.x[i][j] * B.x[j][k]
                C.x[i][k] %= mod
    return C

def powers(A, T):
    # A の T 乗を求める
    E = [Matrix(A.sz) for _ in range(64)]
    E[0] = A
    for i in range(1,62):
        E[i] = multiply(E[i-1], E[i-1])
    F = Matrix(E[0].sz)
    for i in range(F.sz):
        for j in range(F.sz):
            if i == j:
                F.x[i][j] = 1
    for i in range(62,-1,-1):
        if T & (1 << i) != 0:
            F = multiply(F, E[i])
    return F

# Step #1. 入力
N,B,K = map(int,input().split())
C = list(map(int,input().split()))

# Step #2. 行列 A を求める
A = Matrix(B)
for i in range(B):
    for j in range(K):
        nex = (i * 10 + C[j]) % B
        A.x[i][nex] += 1

# Step #3. 行列累乗をする
Z = powers(A, N)

# Step #4. 答えを求める
Answer = Z.x[0][0]
print(Answer)