# 022 - Cubic Cake（★2）
# https://atcoder.jp/contests/typical90/tasks/typical90_v
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/022.cpp

from math import gcd

A,B,C = map(int,input().split())
S = gcd(A, gcd(B, C))
print((A // S - 1) + (B // S - 1) + (C // S - 1))