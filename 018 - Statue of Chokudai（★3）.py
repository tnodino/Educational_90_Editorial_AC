# 018 - Statue of Chokudai（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_r
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/018.cpp

from math import sin, cos, sqrt, atan2, pi

def query(I):
    cx = 0
    cy = -(L / 2.0 * sin(I / T * 2.0 * pi))
    cz = (L / 2.0) - (L / 2.0) * cos(I / T * 2.0 * pi)
    d1 = sqrt(pow(cx - X, 2) + pow(cy - Y, 2))
    d2 = cz
    kaku = atan2(d2, d1)
    return kaku * 180.0 / pi

T = int(input())
L,X,Y = map(int,input().split())
Q = int(input())
for _ in range(Q):
    E = int(input())
    print(query(E))