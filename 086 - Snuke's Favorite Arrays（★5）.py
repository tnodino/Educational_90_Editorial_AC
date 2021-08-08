# 086 - Snuke's Favorite Arrays（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_ch
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/086.cpp

mod = 10**9+7

def bit_zentansaku():
    ways = 0
    for i in range(1<<N):
        bit = [0] * (N+1)
        for j in range(N):
            bit[j+1] = (i // (1 << j)) % 2
        flag = True
        for j in range(Q):
            if bit[x[j]] | bit[y[j]] | bit[z[j]] != w[j]:
                flag = False
        if flag == True:
            ways += 1
    return ways

# Step #1. Input
N,Q = map(int,input().split())
_L = [list(map(int,input().split())) for _ in range(Q)]
X,Y,Z,W = [list(i) for i in zip(*_L)]

# Step #2. Brute Force
x = [0] * Q
y = [0] * Q
z = [0] * Q
w = [0] * Q
Answer = 1
for i in range(60):
    for j in range(Q):
        x[j] = X[j]
        y[j] = Y[j]
        z[j] = Z[j]
        w[j] = (W[j] // (1 << i)) % 2
    ret = bit_zentansaku()
    Answer *= ret
    Answer %= mod
print(Answer)