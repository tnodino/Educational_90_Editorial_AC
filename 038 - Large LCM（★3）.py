# 038 - Large LCM（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_al
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/038.cpp

from math import gcd

A,B = map(int,input().split())
THRESHOLD = 10**18
C = A * B // gcd(A, B)
if C <= THRESHOLD:
    print(C)
else:
    print('Large')