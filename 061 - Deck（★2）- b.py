# 061 - Deck（★2）
# https://atcoder.jp/contests/typical90/tasks/typical90_bi
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/061-02.cpp

from collections import deque

# Step #1. “ü—Í
Q = int(input())
_L = [list(map(int,input().split())) for _ in range(Q)]
T,X = [list(i) for i in zip(*_L)]

# SStep #2. 答えを求める
deq = deque()
for i in range(Q):
    if T[i] == 1:
        deq.appendleft(X[i])
    if T[i] == 2:
        deq.append(X[i])
    if T[i] == 3:
        print(deq[X[i]-1])