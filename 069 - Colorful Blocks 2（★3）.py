# 069 - Colorful Blocks 2（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_bq
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/069.cpp

mod = 10**9+7

N,K = map(int,input().split())
if K == 1:
    print(1 if N == 1 else 0)
elif N == 1:
    print(K % mod)
elif N == 2:
    print(K * (K - 1) % mod)
else:
    print(K * (K - 1) % mod * pow(K - 2, N - 2, mod) % mod)