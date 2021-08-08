# 027 - Sign Up Requests （★2）
# https://atcoder.jp/contests/typical90/tasks/typical90_aa
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/027.cpp

from collections import defaultdict

N = int(input())
Map = defaultdict(int)
for i in range(1,N+1):
    S = input()
    if Map[S] == 0:
        Map[S] = 1
        print(i)