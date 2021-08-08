# 015 - Don't be too close（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_o
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/015.cpp

mod = 10**9+7

def init():
    fact[0] = 1
    factinv[0] = 1
    for i in range(1,N+1):
        fact[i] = (i * fact[i-1]) % mod
        factinv[i] = pow(fact[i], mod - 2, mod) % mod

def ncr(n, r):
    if n < r or r < 0:
        return 0
    return (fact[n] * factinv[r] % mod) * factinv[n-r] % mod

def query(K):
    ret = 0
    # 「N 個中何個選ぶか」を全探索
    # そもそも K が大きいと 1 個か 2 個しか選べないので、そこに着目する
    for i in range(1,N//K+2):
        s1 = N - (K - 1) * (i - 1)
        s2 = i
        ret += ncr(s1, s2)
        ret %= mod
    return ret

# Step #1. 入力
N = int(input())

# Step #2. nCr を求めるために必要な値をメモ（fact / factinv など）
fact = [0] * (N+1)
factinv = [0] * (N+1)
init()

# Step #3. 出力
for k in range(1,N+1):
    Answer = query(k)
    print(Answer)