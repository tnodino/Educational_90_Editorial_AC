# 082 - Counting Numbers（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_cd
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/082b.cpp

mod = 10**9+7

def init():
    # Calculate 10^i
    power10[0] = 1
    for i in range(1,20):
        power10[i] = 10 * power10[i-1]

def f(X):
    if X % 2 == 0:
        v1 = (X // 2) % mod
        v2 = (X + 1) % mod
        return v1 * v2 % mod
    else:
        v1 = ((X + 1) // 2) % mod
        v2 = X % mod
        return v1 * v2 % mod

# Step #1. Initialize / Input
power10 = [0] * 20
init()
L,R = map(int,input().split())

# Step #2. Brute Force by Digit-Size
Answer = 0
for i in range(1,20):
    vl = max(L, power10[i-1])
    vr = min(R, power10[i] - 1)
    if vl > vr:
        continue
    val = (f(vr) - f(vl - 1) + mod) % mod
    Answer += i * val
    Answer %= mod

# Step #3. Output The Answer
print(Answer)