# 075 - Magic For Balls（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_bw
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/075.cpp

def prime_factorial(N):
    rem = N
    p = []
    for i in range(2,N):
        if i * i > N:
            break
        while rem % i == 0:
            rem //= i
            p.append(i)
    if rem != 1:
        p.append(rem)
    return p

# Step #1. Input
N = int(input())

# Step #2. Get Answer
Answer = 0
vec = prime_factorial(N)
for i in range(21):
    if pow(2, i) >= len(vec):
        Answer = i
        break
print(Answer)