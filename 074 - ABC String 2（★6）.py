# 074 - ABC String 2（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_bv
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/074.cpp

N = int(input())
S = input()
Answer = 0
for i in range(N):
    if S[i] == 'b':
        Answer += pow(2, i)
    if S[i] == 'c':
        Answer += pow(2, i) * 2
print(Answer)