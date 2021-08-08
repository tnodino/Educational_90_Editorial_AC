# 080 - Let's Share Bit（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_cb
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/080b.cpp

N,D = map(int,input().split())
A = list(map(int,input().split()))
pop = [0] * (1 << N)
bit = [0] * (1 << N)
for i in range(1,1<<N):
    pop[i] = pop[i >> 1] + (i & 1)
for i in range(N):
    for j in range(1<<i):
        bit[j + (1 << i)] = bit[j] | A[i]
answer = 0
for i in range(1<<N):
    free_digits = D - bin(bit[i]).count('1')
    if pop[i] % 2 == 0:
        answer += (1 << free_digits)
    else:
        answer -= (1 << free_digits)
print(answer)