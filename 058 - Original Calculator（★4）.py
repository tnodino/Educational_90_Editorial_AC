# 058 - Original Calculator（★4）
# https://atcoder.jp/contests/typical90/tasks/typical90_bf
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/058.cpp

def digit_sum(x):
    ans = 0
    while x > 0:
        ans += x % 10
        x //= 10
    return ans

mod = 100000
N,K = map(int,input().split())
nxt = [0] * mod
for i in range(mod):
    nxt[i] = (i + digit_sum(i)) % mod
time_stamp = [-1] * mod
pos = N
cnt = 0
while time_stamp[pos] == -1:
    time_stamp[pos] = cnt
    pos = nxt[pos]
    cnt += 1
cycle = cnt - time_stamp[pos]
if K >= time_stamp[pos]:
    K = (K - time_stamp[pos]) % cycle + time_stamp[pos]
answer = -1
for i in range(mod):
    if time_stamp[i] == K:
        answer = i
print(answer)