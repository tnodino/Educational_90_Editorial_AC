# 065 - RGB Balls 2（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_bm
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/065-02.cpp

mod = 998244353

def ncr(n, r):
    if n < r or r < 0:
        return 0
    return (fact[n] * inv[r] % mod) * inv[n-r] % mod

def init():
    fact[0] = 1
    inv[0] = 1
    for i in range(1,N+1):
        fact[i] = (i * fact[i-1]) % mod
        inv[i] = pow(fact[i], mod - 2, mod) % mod

N = 10**5*5
fact = [0] * (N+1)
inv = [0] * (N+1)
init()

# Step #1. 入力
R,G,B,K = map(int,input().split())
X,Y,Z = map(int,input().split())

# Step #2. 前処理
ar = [0] * (R+1)
ag = [0] * (G+1)
ab = [0] * (B+1)
for i in range(R+1):
    ar[i] = ncr(R, i)
for i in range(G+1):
    ag[i] = ncr(G, i)
for i in range(B+1):
    ab[i] = ncr(B, i)

# Srep #3. 答えを求める
Answer = 0
for i in range(R+1):
    for j in range(G+1):
        rem = K - i - j
        if rem < 0 or rem > B:
            continue
        if i + j > X or j + rem > Y or rem + i > Z:
            continue
        Answer += (ar[i] * ag[j] % mod) * ab[rem] % mod
        Answer %= mod
print(Answer)