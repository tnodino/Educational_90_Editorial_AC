# 080 - Let's Share Bit（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_cb
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/080a.cpp

N,D = map(int,input().split())
A = list(map(int,input().split()))
answer = 0
for i in range(1<<N):
    bit = 0
    conditions = 0
    for j in range(N):
        if (i >> j) & 1:
            bit |= A[j]
            conditions += 1
    free_digits = 0
    for j in range(D):
        if (bit >> j) & 1 == 0:
            free_digits += 1
    if conditions % 2 == 0:
        answer += (1 << free_digits)
    else:
        answer -= (1 << free_digits)
print(answer)