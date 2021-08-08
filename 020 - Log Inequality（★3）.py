# 020 - Log Inequality（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_t
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/020.cpp

A,B,C = map(int,input().split())
E = pow(C, B)
if A < E:
    print('Yes')
else:
    print('No')