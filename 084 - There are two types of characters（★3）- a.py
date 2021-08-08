# 084 - There are two types of characters（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_cf
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/084-01.cpp

N = int(input())
S = '-' + input() + '-'
cnt = 0
vec = []
for i in range(1,len(S)):
    cnt += 1
    if i == len(S) - 1 or S[i] != S[i-1]:
        vec.append((S[i], cnt))
        cnt = 0
ret = 0
for i in range(1,len(vec)):
    ret += vec[i][1] * (vec[i][1] + 1) // 2
print(N * (N + 1) // 2 - ret)