# 090 - Tenkei90's Last Problem（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_cl
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/090-02.cpp

mod = 998244353

def matrix_mult(A, B):
    X = len(A)
    Y = len(B)
    Z = len(B[0])
    ans = [[0] * Z for _ in range(X)]
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                ans[i][k] = (ans[i][k] + (A[i][j] * B[j][k])) % mod
    return ans

N,K = map(int,input().split())
matrix = [[1, 1], [1, 0]]
answer = [[1, 0], [0, 1]]
b = N
while b != 0:
    if b % 2 == 1:
        answer = matrix_mult(answer, matrix)
    matrix = matrix_mult(matrix, matrix)
    b //= 2
print((answer[0][0] + answer[1][0]) % mod)